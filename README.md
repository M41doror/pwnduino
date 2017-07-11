# pwnduino
Hacking with the Arduino Uno!

# 1. Introduction

Many projects have existed out there (check out @samyk !) that turn Arduino HID keyboard devices into USB rubber ducky-likes. However, these devices are already themselves HID devices, and just require a bit of code in the form of Arduino `.ino` scripts to run. At times, many people are not able to obtain Teensy devices, or just simply want to work their existing hardware. With thanks to @ZP4, @Dr-D12345 and @thatguy1675, we were able to built a framework that turns Arduino Unos into malicious HID devices, dubbed __pwnduino__, and effectively hack and gain escalated privilege and persistence on an open computer.

__pwnduino__ is still a __work-in-progress__. Development for it, however, is very active.

# 2. How it Works

An Arduino Uno (version rev. 3) has an `atmega16u2` chip on its board. We can flash this chip using a program called `dfu-programmer`, available on Linux distributions

    sudo apt-get install dfu-programmer

or, build from source [here](https://dfu-programmer.github.io/).

We get two `.hex` files, one for a USB serial device, and one for an HID keyboard device. __pwnduino__ automates that process, first flashing the Arduino Uno into a serial device. However this still does require a bit of __user input__, as you will be required to do what is known as placing the Arduino into __DFU Mode__. In order to do this, you can take
a jumper wire, and short the __GND pin__ and the top left __ICSP pin__.

![](http://i.imgur.com/B9x4Cyf.jpg)

After doing so, the Arduino's onboard LED will light up for a few short moments. Your Arduino will be ready to be flashed. __pwnduino__ will do this automatically.

Afterwards, you can still upload scripts to the Arduino. Once the Arduino is flashed into a HID device, it will automatically execute that code. Several scripts have been included, however, you can still write your own.

After uploading a script, __pwnduino__ will flash your Arduino into a keyboard HID device. Plug it into a vulnerable, and open computer, and watch the magic (not really) happen.

# 3. Downloading and Installation

    git clone https://github.com/ex0dus-0x/pwnduino
    cd /path/to/pwnduino
    python installer.py

Super E-Z! Even a script kiddy can do it.

After installation:

    python pwnduino.py

Plug in your Arduino Uno, and have fun!

# 4. Troubleshooting

LOL, No one used this yet. Of course there will be problems, but :P

# 5. TODO

This project still presets to us A LOT of potential issues, and we wish to improve upon them. Hacking with the Arduino Uno has already been seen previously after the introduction of the Teensy and the Rubber Ducky. The Arduino Uno is not the only model of the Arduino family that can be potentially hacked and turned into a malicious HID, but also other models, such as the Mega. These challenges present to us countless possibilities and even potential hardware modifications that enable us to enhance the overall effective of the program.
