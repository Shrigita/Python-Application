import time
import threading

def EvenFactors(No):
    Sum = 0
    for i in range(1,int((No)/2) + 1):
            if(No % i == 0):
                Sum = Sum + i
    print("Addition of even number Factors :",Sum)
        
def OddFactors(No):
    Sum = 0
    for i in range(1,int((No)/2) + 1):
            if(No % i == 0):
                Sum = Sum + i
    print("Addition of odd number Factors :",Sum)
    
     

def main():
    print("Demonstartion of Parallel programming using multiple threads")
    print("Enter Even Number to sum of factors")
    Number1 = int(input())

    print("Enter Odd Number to sum of factors")
    Number2 = int(input())

    p1 = threading.Thread(target = EvenFactors, args = (Number1,))
    p2 = threading.Thread(target = OddFactors, args = (Number2,))

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