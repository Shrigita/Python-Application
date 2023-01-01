import time
import threading

def Evenlist(Arr):
    sum = 0
    for i in range(0,len(Arr),1):
            if(Arr[i] % 2 == 0):
                sum = sum + Arr[i]

    print("Summation of Evenlist :",sum)

def Oddlist(Arr):
    sum = 0
    for i in range(0,len(Arr),1):
            if(Arr[i] % 2 != 0):
               sum = sum + Arr[i]
    print("Summation of Oddlist :",sum)
     

def main():
    print("Demonstartion of Parallel programming using multiple threads")
    print("Enter Number of element in list")
    size =int(input())
    Arr = []
    print("Please Enter the values")
    for i in range(0,size):
        no = int(input())
        Arr.insert(i,no)
    

    p1 = threading.Thread(target = Evenlist, args = (Arr,))
    p2 = threading.Thread(target = Oddlist, args = (Arr,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print("End of main")

if __name__ == "__main__":
    start_time = time.process_time()
    main()
    end_time = time.process_time()
    print("Execution time is : ",end_time - start_time)