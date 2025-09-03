# Programming Pygame Zero to make images move and play sounds

Pygame Zero can be installed using pip, the Python package installer. Open a terminal window (in VSCode, or the program cmd on Windows or Terminal on Mac). Type "pip install pgzero".  

To run Pygame Zero code, use the command "pgzrun" in the terminal, rather than the usual "python" command.

Pygame Zero opens a window and draws a circle:
```py
{{#include pygamezero_open.py}}
```

Pygame Zero draws eyes that follow the mouse:
```py
{{#include pygamezero_eyes.py}}
```

Pygame Zero draw the mouse position as text:
```py
{{#include pygamezero_mousetext.py}}
```

Pygame Zero Piano:
```py
{{#include pygamezero_piano.py}}
```

Pygame Zero open a serial port and draw the number received (use "pip install pyserial" to get the serial package):
```py
{{#include pygamezero_serialtext.py}}
```
and the code that would run on the Pico to send the data:
```py
{{#include picotopgz_serialtext.py}}
```

