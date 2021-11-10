
print("\n")
print("Apple weight calculater")
print("------------------------")
apple = input("Enter how many apples : ")
weightunit = input("you want kg or lbs? : K or L")
if weightunit == "K":
    applekg = float(apple)/5
    print("Weight of your apple is : " + str(applekg) + "Kg")
    print("\n")
elif weightunit == "L":
    applekg = (float(apple)/5) * 2.2
    print("Weight of your apple is : " + str(applekg) + "Kg")
    print("\n")

