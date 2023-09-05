# Programming the Pico in Circuit Python

The Raspberry Pi Pico microcontroller breakout board is a powerful and inexpensive device that can be programmed in Circuit Python or in C. On this page, we will program it with Cicruit Python.

When the Pico is plugged into a computer for the first time it will enumerate as a thumb drive called RPI-RP2. This is the default, blank configuration of the board. The board can be placed into this mode while holding the BOOT button while plugging the USB cable in. 

To install Circuit Python, download a precompiled version from the [Circuit Python website](https://circuitpython.org/board/raspberry_pi_pico_w/). Copy the file with a .uf2 extension onto the RPI-RP2 drive. The drive will dissappear and then reappear as a new thumb drive called CIRCUITPY. On this drive is a file called code.py, a folder called lib, and two other text files.

To edit the code, open code.py in a text editor, edit the file, and after clicking save, the new file will start to run. The board will also enumerate as a virtual serial port, and the port can be opened in a terminal emulation program to send and recieve data.

After the code is saved, it will remain on the board forever. Unplug the USB and plug in a battery and the code will immediately begin running again! The code doesn't really end either, typically the code will loop forever, until power is removed.

It can be annoying to use a general text editor and terminal emulator program, so instead you could use an IDE developed for Circuit Python called [Mu](https://codewith.mu/), pronounced "moo". Mu contains a text editor, a terminal emulator, and some other goodies like standard Python and pygame zero for graphics.

After you open Mu, click the Mode button in the top right and switch to CircuitPython. Click the load button and open code.py in the CIRCUITPY drive. One downside to the design of the Circuit Python system si that the code that runs on the board must be named code.py. If there is no file called code.py then nothing will run, and putting another .py file in the drive will be ignored unless it is run as a function from code.py. Not a horrible problem, but annoying when you have a few different programs to try out and you must constantly rename them.

## REPL

Before editing code.py we can interact with Circuit Python using Read-Evaluate-Print-Loop, or REPL mode. Press the Serial button and click inside the CircuitPython REPL window at the bottom of the screen. Type any key and the board will enter REPL mode and present three carrots, ">>>". This is your clue to interact directly with Python. 

In REPL mode you can create variables, do math or loops, and test code snippets. You wouldn't want to work in REPL, it is too slow, saving code in a file is much more convinient, but REPL is useful for debugging.

To exit REPL and run code.py, type CTRL-D. If the code ends, the Serial window will prompt you to type any key to enter REPL or type CTRL-D to run the code again. Usually the code is in an infinite loop and will not end, so to cause the code to end and enter REPL at any time you can type CTRL-C. This is the best way to stop and restart the code.

## Try some code!

```py
{{#include print_hello.py}}
```

```py
{{#include blink.py}}
```

```py
{{#include fade.py}}
```

```py
{{#include read_button.py}}
```

```py
{{#include debounce.py}}
```

```py
{{#include read_voltage.py}}
```

```py
{{#include servo.py}}
```

You can find all of the functions included with CIrcuit Python in REPL mode by typing import [tab key].

```py
{{#include neopixel_write.py}}
```

Most external components do not have code included with Circuit Python. They must be downloaded and copied to the CIRCUITPY/lib folder to work. There isn't enough space on the board for all of the libraries, only copy the libraries you need!

The libraries come as a zip folder from [Circuit Python](https://circuitpython.org/libraries). Download the folder that cooresponds to your version of Circuit Python and unzip the folder. Libraries are found in the /lib folder, sometimes as files with .mpy extensions or as entire folders.

```py
{{#include neopixel.py}}
```

```py
{{#include mma8451.py}}
```