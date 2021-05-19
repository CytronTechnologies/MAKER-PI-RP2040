import board
import audiocore
import audiopwmio
import digitalio
import time

# Initialize buttons
button1 = digitalio.DigitalInOut(board.GP20)
button1.switch_to_input(pull=digitalio.Pull.UP)

# Global variables
button1_pressed = False

# Initialize audio
data = open("maker.wav", "rb")
wav = audiocore.WaveFile(data)
audio = audiopwmio.PWMAudioOut(board.GP22)


while True:
    if not button1.value:
        print("Button pressed")
        print("Playing audio...")
        audio.play(wav)
        time.sleep(2)
        audio.stop()   
        print("Stopped")
    else:
        pass
    
    time.sleep(0.1) # sleep for debounce