class BookStore: 
   NoOfBooks = 0
   def __init__(self,A,B):
        print("Inside init method")
        self.Name = A
        self.Author = B
        BookStore.NoOfBooks += 1

   def Display(self):
      print("Name of Book :",self.Name)
      print("Name of Author :",self.Author)
      print("No of Books :",BookStore.NoOfBooks)
        
def main():
   obj1 = BookStore("Linux Programming Lang.","Robert Love")
   obj1.Display()

   obj2 = BookStore("C Programming","Dennis Richee")
   obj2.Display()

if __name__ == "__main__":
    main()