# use pygame zero in Mu to draw graphics and play sounds

# must import pyserial into Third Party Packages using Mu Administration (gear) button in bottom right
import serial  
# the name of your port here. On Windows, COM#, on Mac, /dev/tty.usbmodem#
ser = serial.Serial('/dev/tty.usbmodem14201') 
print('Opening port: ')
print(ser.name)

# size of the screen to draw
WIDTH = 500
HEIGHT = 500

# open an image from the mu_code/images folder
my_img = Actor('rpi', center = (250,250))

# draw() is called automatically
def draw():
    screen.clear()
    my_img.draw()

# update is called automatically
def update():
    n_bytes = ser.readline() # read a line from the serial port, as bytes
    s = str(n_bytes) # turn the bytes into a string
    #print(s)
    #print(len(s))
    
    # lots of crazy stuff in the string, look for your specific message
    if (len(s)>30):
        if (s[26] == "A"):
            #print("A")
            #sounds.boinggg.play() # play a sound from the mu_code/sounds folder, will overlap itself
            # play a sound from mu_code/music, but only if it is not already playing
            if music.is_playing('boinggg.wav'):
                pass
            else:
                music.play_once('boinggg.wav')
        if (s[26] == "B"):
            #print("B")
            result = s[s.find('B')+1:s.find(',')] # pull the number out of the string
            #print(result)
            n_int = int(result)
            #print(n_int)
            my_img.angle = 360*n_int / 65536 # scale the analog read to angle

# this function is automatically called when the keyboard is pressed
def on_key_down(key):
    #print(key)
    if key == keys.A:
        #print("a")
        ser.write(("a\n").encode()) # print to the serial port
    if key == keys.S:
        #print("s")
        ser.write(("s\n").encode())

