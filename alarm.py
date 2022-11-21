import time
import os
from pygame import mixer
from random import randint
from leetcodeAPI import LeetcodeApiStuff
from maintenance import * 
from datetime import datetime, timedelta 

class Alarm(file_handler,LeetcodeApiStuff):
    def __init__(self)->None:
        """Loop forever checking if it is time to ring"""
        try:
            self.conf_writer()
        except:
            pass
        finally:
            self.time = self.conf_reader()
       

        #Getting time and converting it into second format
        seconds_hms = [3600, 60, 1]
        now = datetime.now()
        currentTimeInSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

        #Calculating the time left to ring
        secondsUntilAlarm = self.time - currentTimeInSeconds
        
        #If the time already passed add a day
        if secondsUntilAlarm < 0:
            secondsUntilAlarm += 86400 # number of seconds in a day

        print("Alarm is set!")

        time.sleep(secondsUntilAlarm)
        self.api_response = self.init_API()
        self.ring() # recall to turn off the alarm the user must be able to solve leetcode or codepen challenges

    def ring(self)->None:
        record = self.count_solved_problems()
        verif = self.verify(record)
        mixer.init()
        mixer.music.load(r'./Tone/Soft-Wake-Up.wav') #change this line of code with whatever audio file you would like to play
        mixer.music.play()
        while not verif:
            verif = self.verify(record)            
        mixer.music.fadeout(2500)
        print('Alarm successfully shutdown')

        

if __name__ == "__main__":
    handler = file_handler()
    handler.log_run()
    Alarm()
    handler.log_success()

    
