print("Demonstration of list : ")

#Data : Heterogeneous
#Ordered : Yes
#Indexed : Yes
#Mutable : Yes
#Duplicate :Yes

data = [11,21,51,101,11,21]
data1 = [11, 90.8, True, "Hello"]   #Heterogeneous

print("Heterogeneous Data : ",data1)
print("Data is ordered:",data1)     
print("Data is index 2 :",data1[2])
print("Data with duplicate element :",data)

print("List is Mutable")
data.append(201)
print("Data after append ",data)

data.pop()
print("Data after pop ",data)
