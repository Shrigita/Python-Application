def Display(Value):
    cnt = 1
    while(Value >= cnt):
      print(cnt,end ='\t')
      cnt = cnt + 1
      
    print()

def main():
   print("Enter Number :")
   No =int(input())
   Display(No) 

if __name__ == "__main__":
    main()