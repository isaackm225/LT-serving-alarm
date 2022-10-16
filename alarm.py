import vlc
import os
from leetcodepy import LeetcodeApiStuff
from random import randint

class Alarm():
    def __init__(self) -> None:
        self.zik = './Alarm/Tone/'   #audio folder
        
    def play(self)->None:
        files=os.listdir(self.zik)
        idx = randint(0,len(files)-1)
        media = vlc.MediaPlayer(f'{self.zik}{files[idx]}')
        #print(files[idx])
        media.play()

if __name__ == "__main__":
    Alarm().play()


