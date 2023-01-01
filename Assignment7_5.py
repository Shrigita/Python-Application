import time
import threading

def thread1(No):
    for i in range(1,No+1,1):
        print(i)
   

def thread2(No):
    for i in range(No,0,-1):
        print(i)
    

def main():
    print("Demonstartion of Parallel programming using multiple threads")
    Number =50


    p1 = threading.Thread(target = thread1, args = (Number,))
    p2 = threading.Thread(target = thread2,args = (Number,))

    p1.start()
    p1.join()
    
    p2.start()
    p2.join()


    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)