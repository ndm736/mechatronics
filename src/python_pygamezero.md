# Programming Pygame Zero to interface with USB communication from the Pico

Python, on your computer, by itself is not great at drawing graphics that update quickly or playing sounds, but the [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/) framework is setup for this purpose.  

Pygame Zero can be installed using pip, the Python package installer. Open a terminal window (in VSCode, or the program cmd on Windows or Terminal on Mac). Type "pip install pgzero".

The test data that the Pico prints to the computer and recieves from the keyboard is sent through a type of USB communication called CDC, which emulates anolder protocol usually refered to as "serial" communication. In serial communication, the USB device is given a name called a port, which can be opened to read and write text data. In Windows, the port name is typically the word COM, followed by a number, like COM3 or COM4. You can find the name in the program Device Manager. In Mac and Linux, the port name is typically the word /dev/tty., followed by the word usbserial or usbmodem, followed by a number, like /dev/tty.usbmodem14201. You can find the name by opening the program terminal, and typing "ls /dev/tty.*", and the available ports will be listed.

Ports can only be open by one program at a time, so close the port in Putty or Screen before trying to open the port with Pygame Zero code.

The trick for getting a Pico to communicate with Pygame Zero code is to invent a communication protocol, so that the messages can de decyphered. 

In the following example, the Pico constantly prints the letter "b" followed by a number read from the ADC. If a pushbutton is pressed, the letter A is printed. If the letter "a" is recieved, the servo angle in incremented. If the letter "b" is recieved, the servo angle is decremented. A special python package, nonblocking_serialinput is used from the [Circuit Python Community Bundle](https://circuitpython.org/libraries) to be able to read messages from the computer without calling input(), which would cuase the code to wait until a message was recieved without being able to move on.

The Pygame Zero code opens the port and jumps back and forth between the update() and draw() functions. The ser.readline() function reads the messages from the Pico, but note that the messages contain lots of characters that you usually do not see in the Serial window, so you have to find your message in the string.

Pico code:
```py
{{#include pico_pygamezero_demo.py}}
```

Pygame Zero code:
```py
{{#include pygamezero_pico_demo.py}}
```
