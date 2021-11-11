
print("\n")
print("Apple scale")
print("===========")

apple = input("Enter how many apples you bought: ")
weightunit = input("Select the metric : type K (kg) or L (lbs) : ")
if weightunit == "K" or weightunit =="k":
    applekg = float(apple)/5
    print("\n")
    print("Weight of your " + str(apple) + " apples is : " + str(applekg) + " Kg")
    print("\n")
elif weightunit == "L" or weightunit=="l":
    applekg = (float(apple)/5) * 2.2
    print("\n")
    print("Weight of your " + str(apple) + " apples is : " + str(applekg) + " Lbs")
    print("\n")

    

