#Normal Function/Named Function

def Add(No1,No2):
    return No1+No2

#Lambda Function/ Unmamed Function
#lambda parametrs : body

AddFunction = lambda A,B :A+B

Ans1 = Add(10,11)
Ans2 = AddFunction(10,11)

print("Addition using normal function :",Ans1)   #21
print("Addition using lambda function :",Ans2)   #21

print("Type of lambda function is :",type(AddFunction))   #function
print("Type of Normal function is :",type(Add))           #function