print("Demonstration of Dictionary : ")

Batches = {"PPA":18000, "LB":16700, "Python":16500, "Angular":15000}

print("Data of Dictionary :",Batches)
print("Data Traversal using for loop")
for x in Batches:
    print(x)


print("Data Traversal using for loop with value")
for x in Batches:
    print(x,":",Batches[x])

print("Data Traversal using for loop nd get method with value")
for x in Batches:
    print(x,":",Batches.get(x))

keysBatches = Batches.keys()
print(keysBatches)
print(type(keysBatches))

valueBatches = Batches.values()
print(valueBatches)
print(type(valueBatches))

