from pygame import mixer
import time
import os
from leetcodepy import LeetcodeApiStuff
from random import randint

def ring()->None:
    LTcode = LeetcodeApiStuff()
    record = LTcode.count_solved_problems()
    verif = LTcode.verify(record)
    mixer.init()
    mixer.music.load(r'.\Tone\Soft-Wake-Up.wav')
    while not verif:
        mixer.music.play()
        print('Playing')
        mixer.music.set_volume(1.0)
        time.sleep(120)
        mixer.music.fadeout(15)
        print('Fading out')
        time.sleep(20)
        print('Verifying')
        verif = LTcode.verify(record)
        print(verif)
        

if __name__ == "__main__":
    ring()
