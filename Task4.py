import schedule
import time
import datetime
import sys

a = 0
def Task_Schedule():
    a =+ 1
    if(a == 10):
        sys.exit()

def Task_Minute():
    print("Hello...")
    


def main():
    print("Inside task schedular")
    print("Current time is : ",datetime.datetime.now())
    
    schedule.every(1).minutes.do(Task_Minute)
    

    
    while(1):
        Task_Schedule()
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__" :
    main()