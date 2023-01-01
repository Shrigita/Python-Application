import math
class Circle:
    math.pi = 3.14
    def __init__(self):
        Radius = 0.0
        Area = 0.0
        Circumference = 0.0

    def Accept(self):
        print("Enter the Radius Plz :")
        self.Radius = float(input())
    
    def CalculateArea(self):
        self.Area = math.pi * self.Radius * self.Radius
       
    def CalculateCircumference(self):
        self.Circumference = 2 * math.pi * self.Radius

    def Display(self):
        print("Radius of Circle :",self.Radius)
        print("Area of Circle :",self.Area)
        print("Circumference of Circle :",self.Circumference)

def main():
    obj1 = Circle()
    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

if __name__ =="__main__":
    main()

    
