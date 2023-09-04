# Programming the Pico in Circuit Python

The Raspberry Pi Pico microcontroller breakout board is a powerful and inexpensive device that can be programmed in Circuit Python or in C. On this page, we will program it with Cicruit Python.

When the Pico is plugged into a computer for the first time it will enumerate as a thumb drive called RPI-RP2040. This is the default, blank configuration of the board. The board can be placed into this mode while holding the BOOT button while plugging the USB cable in. 

To install Circuit Python, download a precompiled version from CP. Cope the file onto the RPI-RP2040 drive. The drive will dissappear and then reappear as a new thumb drive called CIRCUITPY. On this drive is a file called code.py, a folder called lib, and a few other text files.

To edit the code, open code.py in a text editor, edit the file, and after clicking save, then new file will start to run. The board will also enumerate as a virtual serial port, and the port can be opened in a terminal emulation program to send and recieve data.

After the code is saved, it will remain on the board forever. Unplug the USB and plug in a battery and the code will immediately begin running again!

It can be annoying to use a general text editor and terminal emulator program, so instead you could use an IDE developed for Circuit Python called Mu. Mu contains a text editor, a terminal emulator, and some other goodies like standard Python and pygame zero for graphics.

