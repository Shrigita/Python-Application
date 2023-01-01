import time
import threading

def small(String):
    count = 0
    for i in String:
        if(i.islower() == True):
            count +=1
    print("Small letter of Sring :",count)


def capital(String):
    count = 0
    for i in String:
        if(i.isupper() == True):
            count +=1
    print("Capital letter of Sring :",count)

def digit(String):
    count = 0
    for i in String:
        if(i.isdigit() == True):
            count +=1
    print("Digits of Sring :",count)


def main():
    print("Please Enter String :")
    String = input()

    p1 =threading.Thread(target = small, args =(String,))
    p2 =threading.Thread(target = capital, args =(String,))
    p3 =threading.Thread(target = digit, args =(String,))
    
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("End of main")


if __name__ == "__main__":
    start_time =time.process_time()
    main()
    end_time =time.process_time()
    print("Execution time :",end_time -start_time)