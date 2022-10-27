from datetime import datetime

class logwriter():
    def write_log(self):        
        with open("log.txt","a+") as log:
            log.write(f"The alarm ran on {datetime.now()}")
        
    def log_success(self):
        with open("log.txt","a+") as log:
            log.write(f"Successfully solved leetcode problem {datetime.now()}")
        
