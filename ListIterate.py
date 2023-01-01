print("Demonstration of list Iteration")

Data = [11,21,51,101]
print("Output Using for : ")
for no in Data:
    print(no,end=" ")
print()


print("Output Using for with index :")
for i in range(0, len(Data)):
    print(Data[i],end=" ")
print()

print("Output Using while with index :")
i = 0
while(i < len(Data)):
    print(Data[i],end=" ")
    i+=1 
print()