############## Python Modules ##############
import os, sys, argparse, signal
from time import sleep
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
FAIL = "[" + R + "FAILED!" + W + "]"
SUCCESS = "[" + G + "SUCCESS" + W + "]"

# Cowsay!
header = LP + """

  ______________________________________
| pwnduino-client.py - Turn your Arduino |
| into a pwnDuino!                       |
  --------------------------------------
         \   ^__^
          \  (oo)\_______
             (__)\       )\/
                 ||----w |
                 ||     ||

""" + W

############## ############## ##############


############## Interrupt Handler ##############
def handler(signal, frame):
    print R + "Interrupted! Stopping..." + W
    os.system("rm -r src/dmesg.txt &>/dev/null")
    sys.exit(1)

signal.signal(signal.SIGINT, handler)
############## ############## ##############


############## Command-line Parser ##############
parser = argparse.ArgumentParser(description='Turn Arduino into a pwnDuino')
parser.add_argument('--check-deps', dest="dep", action="store_false", help="Check if dependencies are installed")
args = parser.parse_args()

dep = args.dep

if dep is False:
    print "Checking dependencies"
    raw_input()
else:
    pass
############## ############## ##############


############## Actual Code ##############
print header

os.system("dmesg -c > /dev/null")

print LC + "Welcome to pwnduino-client! Please plug in (or plug out and plug in again) your Arduino Uno. Press Enter to continue" + W
enter = raw_input("")

try:
    os.system("dmesg > src/dmesg.txt")
    print O + "Checking..." + W
    sleep(3)
    fileHandle = open ( 'src/dmesg.txt',"r" )
    lineList = fileHandle.readlines()
    fileHandle.close()
except KeyboardInterrupt:
    print R + "Interrupted! Killing..."


for x in range(-4, 0):
    found = False
    try:
        print lineList[x]
        found = True
    except IndexError:
        print O + "[!] Arduino not detected in dmesg [!]" + W
        found = False


if found == True:
    print LG +  "Arduino found!" + W
elif found == False:
    noduino = raw_input(R + "[!] There seems to be no Arduino detected. Would you like to continue? (y/n) [!] " + W)
    if noduino == "y":
        pass
    elif noduino == "n":
        sys.exit(1)
    else:
        print "Oops! No input!"

os.system("rm -r src/dmesg.txt")

print O + "[*] On the Arduino, please short GND and reset. Press Enter once completed [*]"
enter = raw_input()
print O + "[*] Performing Initial Flashing... [*]" + W
os.system("dfu-programmer atmega16u2 erase")
os.system("cd src && dfu-programmer atmega16u2 flash --debug 1 Arduino-usbserial.hex")
os.system("dfu-programmer atmega16u2 reset")
print LG + "Done! Plug cycle the Arduino and press Enter once that is finished" + W
enter = raw_input()


print "==================================="
print "|| (1) Windows 7/8/10            ||"
print "|| (2) Mac OS X / Darwin         ||"
print "|| (3) Unix/Linux-based Distros  ||"
print "==================================="

platform = raw_input(LC + "[>] What is the platform you are targeting? " + W )

if platform == "1":
    print  LG + "[*] Initial Windows 7/8/10 sketch build... [*]"
    print LO + "Uploading sketch to Arduino..." + W
    os.system("cd src/ && arduino --upload windows_hid.ino")
elif platform == "2":
    print LG + "Not yet..."

print LB + "Flashing Arduino into HID Keyboard Device..." + W
print LO + "[*] On the Arduino, please short GND and reset. Press Enter once completed [*]" + W
enter = raw_input()
os.system("dfu-programmer atmega16u2 erase")
os.system("cd src/ && dfu-programmer atmega16u2 flash --debug 1 Arduino-keyboard.hex")
os.system("dfu-programmer atmega16u2 reset")
print LG + "[!] Done! Unplug your brand-new " + LB + "pwnduino" + LG + " and Hack the Gibson!" + W
