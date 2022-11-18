from datetime import datetime

class file_handler():
    def log_run(self):        
        with open("log.txt","a+") as log:
            log.write(f"The alarm ran on {datetime.now()}")
        
    def log_success(self):
        with open("log.txt","a+") as log:
            log.write(f"Successfully solved leetcode problem {datetime.now()}")

    def conf_reader(self):
        with open("time.txt", "r") as ftime:
            time = ftime.read().strip()
            time = int(time)
            return time

    def conf_writer(self):
        with open("time.txt", 'x') as ftime:
            time = self.prompt()
            ftime.write(str(time))

    def prompt(self):
        invalid = True
        while invalid:
            # Get a valid user input for the alarm time
            print("Set a valid time for the alarm (Ex. 06:30)")
            userInput = input(">> ")
            # For example, this will convert 6:30 to an array of [6, 30].
            alarmTime = [int(n) for n in userInput.split(":")]
            # Validate the time entered to be between 0 and 24 (hours) or 0 and 60 (minutes)
            if alarmTime[0] >= 24 or alarmTime[0] < 0:
                invalid = True
            elif alarmTime[1] >= 60 or alarmTime[1] < 0:
                invalid = True
            else:
                invalid = False
        # Number of seconds in an Hour, Minute, and Second
        seconds_hms = [3600, 60, 1]
        # Convert the alarm time to seconds
        alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(alarmTime)], alarmTime)])
        return alarmSeconds
