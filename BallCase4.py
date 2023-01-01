from sklearn import tree

#load the dataset
#Rough :1
#Smooth :0

#Cricket :2
#Tennis : 1

def BallPredictor(weight,surface):
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj =tree.DecisionTreeClassifier()
    obj =obj.fit(Features, Labels)

 
    ret = obj.predict([[weight,surface]])
    if ret == 1:
        print("Your object is look like a Tennis Ball ")
    else :
        print("Your object is look like a Cricket Ball")

def main():
    print("------------Ball Predictor Case Study-----------")

    print("Please Enter the Weight of your object in Gram")
    weight = int(input())

    print("Please enter type of surface of your object (Rough/Smooth)")
    surface = input()

    if surface.lower() =="rough":
        surface = 1
    elif surface.lower() =="smooth":
        surface = 0
    else:
        print("Invalid type of surface ")
        exit()

    BallPredictor(weight ,surface)

if __name__ =="__main__":
    main()