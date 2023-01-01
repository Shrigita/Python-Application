
def Area(Radius,PI = 3.14):
    Result = PI * Radius * Radius
    return Result

def  main():
    Rvalue = 10.5
    PIvalue = 3.14

    #Positional Argument
    Ans = Area(Rvalue, PIvalue)         # Ans = Area(10.5,3.14)
    print("Area of circle is :",Ans)

    #keyword Argument
    Ans = Area(PI = PIvalue, Radius = Rvalue)   # Ans = Area(3.14,10.5)
    print("Area of circle is :",Ans)
    
    #Positional and  Second isDefault
    Ans = Area(10.5)      #Ans = Area(10.5)
    print("Area of circle is :",Ans)
    
    #keyword argument and second is default
    Ans = Area(Radius = 10.5)      #Ans = Area(10.5)
    print("Area of circle is :",Ans)

    #keyword argument
    Ans = Area(PI = 7.10, Radius = 10.5)      #Ans = Area(10.5,7.10)
    print("Area of circle is :",Ans)



if __name__ =="__main__":
    main()