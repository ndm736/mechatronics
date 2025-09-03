# Embedded Programming

Many design problems can be solved with circuits. But as the solution becomes more complicated, changing functionality can require a large amount of circuit to take apart, redesign, and rebuild. It can be faster to add a programmable element to the design, and change the code very rapidly while prototyping. The component that does this is a microcontroller. A microcontroller is a computer system on a chip that is designed to run code with relatively small amounts of power. Modern microcontrollers can be infinitely reprogrammed, and come in a variety of sizes, speeds, and amount of memory.

Most microcontrollers do not fit into a breadboard, they are too small with too many pins. Components like this can be purchased presoldered onto a PCB called a breakout board, that makes it easier to use a component with a breadboard. A lot of these designs are open source hardware and software, so they are inexpensive and have large communities for support.

## Arduino

Perhaps the most popular microcontroller system is Arduino. Arduino is both a brand, the name of the integrated development environment (IDE) used to program the device, potentially the name of the breakout board, and sometimes used to describe the code on the microcontroller. The most popular Arduino is the Arduino Uno, but there are hundreds of other Arduino's with different shapes, speeds, and prices, each to fit a specific type of project. The advantage of using Arduino is that the code used on one breakout board can be easily applied to a different breakout board, if for instance you wanted to add wifi or bluetooth or more memory later on. There are many caveats to this but in general Arduino is a very flexible and capable system.

Arduino code is C/C++, saved in a file with a .ino extension. This language has a learning curve that could prevent a beginner from rapidly prototyping. Luckily a large amount of sample code is provided with the IDE, but learning to program can be labor intensive.

## Circuit Python

A more recent project has ported the programming language Python to microcontrollers, called micropython. Python is one of the most popular programming languages, so you may already know some Python, or you can learn Python faster than you could C with so much free learning websites availible for Python online.

One version of micropython is Circuit Python, which maintains large libraries of sample code for the most popular microcontroller boards and breakout boards. 

## C vs Python

Most boards that run Circuit Python could also be programmed in C with Arduino. When trying to decide between using Python or C for a progject, consider the complexity of the project and how fast you would like to prototype. Python will be faster to get the project running, and the Python libraries contain nice high level functions, like FFT and performing communication over the internet. C code can potentially run 100 times faster, and gives more access to the low level hardware of the microcontroller. 

## Raspberry Pi vs Arduino

Another popular system is the Raspberry Pi single board computer system. The Raspberry Pi is a computer, with ten times the speed and one thousand times the memory of a microcontroller. But the Raspberry Pi runs an operating system, so a dedicated program might not run better than the same program on a microcontroller. Raspberry Pi's are also more expensive, take more gear to use, and can be hard to source. My recommendation is, if you need graphics on an HDMI monitor or need to play high quality sound, try a Raspberry Pi. Otherwise you can probably do just as well with a less expensive and easier to use Arduino or micropython board.

## Courses to take

Northwestern offers several courses on using microcontrollers:

- ME333: Introduction to Mechatronics
- ME433: Advanced Mechatronics
- DSGN297: Smart Electronics in Design
- DSGN495: Designing Product Interations (DPI)