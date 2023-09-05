# Programming the Pico in Circuit Python

The Raspberry Pi Pico microcontroller breakout board is a powerful and inexpensive device that can be programmed in Circuit Python or in C. On this page, we will program it with Cicruit Python.

When the Pico is plugged into a computer for the first time it will enumerate as a thumb drive called RPI-RP2. This is the default, blank configuration of the board. The board can be placed into this mode while holding the BOOT button while plugging the USB cable in. 

To install Circuit Python, download a precompiled version from the [Circuit Python website](https://circuitpython.org/board/raspberry_pi_pico_w/). Copy the file with a .uf2 extension onto the RPI-RP2 drive. The drive will dissappear and then reappear as a new thumb drive called CIRCUITPY. On this drive is a file called code.py, a folder called lib, and two other text files.

To edit the code, open code.py in a text editor, edit the file, and after clicking save, the new file will start to run. The board will also enumerate as a virtual serial port, and the port can be opened in a terminal emulation program to send and recieve data.

After the code is saved, it will remain on the board forever. Unplug the USB and plug in a battery and the code will immediately begin running again! The code doesn't really end either, typically the code will loop forever, until power is removed.

It can be annoying to use a general text editor and terminal emulator program, so instead you could use an IDE developed for Circuit Python called [Mu](https://codewith.mu/), pronounced "moo". Mu contains a text editor, a terminal emulator, and some other goodies like standard Python and pygame zero for graphics.

After you open Mu, click the Mode button in the top right and switch to CircuitPython. Click the load button and open code.py in the CIRCUITPY drive. One downside to the design of the Circuit Python system si that the code that runs on the board must be named code.py. If there is no file called code.py then nothing will run, and putting another .py file in the drive will be ignored unless it is run as a function from code.py. Not a horrible problem, but annoying when you have a few different programs to try out and you must constanly rename them.



