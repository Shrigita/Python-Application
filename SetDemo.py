print("Demonstration of Set : ")

#Data : Heterogeneous
#Ordered : No
#Indexed : No
#Mutable : Yes
#Duplicate :No

data = {11,21,51,101,11,21}          #duplicate
data1 = {11, 90.8, True, "Hello"}  #Heterogeneous

print("Heterogeneous Data : ",data1) 
print("Data is Unordered:",data1)     
#print("Data is Unindex 2 :",data1[2])
print("Data with unic element :",data)
print(len(data))


print("Set is Mutable")
#insert element in set
data.add(211)
print("Data After insertion",data)

#Remove Element
data.remove(211)
print("Data After removal",data)

#if element is not available nd user remove the element then use discard
data.discard(201)
print("Data After discard",data)
