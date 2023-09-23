# play a .wav sound file
# copy the .wav file to the CIRCUITPY/ drive
# .wav file can be mono or stereo, <=22kHz sample rate, 16bit wav format, try the program Audacity to edit files
# note Pico W memory is 2Mbyte, so sound files need to be small
import audiocore
import board
import audiobusio
import time

wave_file = open("StreetChicken.wav", "rb") # from https://cdn-learn.adafruit.com/assets/assets/000/057/801/original/StreetChicken.wav?
wave = audiocore.WaveFile(wave_file)
audio = audiobusio.I2SOut(board.GP0, board.GP1, board.GP2) # MAX98357, I2S pins BCLK, LRC, DIN

while True:
    print("wav file start")
    audio.play(wave)
    while audio.playing:
        pass # code here that should only happen while wav is playing
    print("wav file done")
    time.sleep(3)

