# from flask import Flask
# app = Flask(__name__)
# @app.route('/<int:number>/')
# def incrementer(number):
#     return "Incremented number is " + str(number+1)
# @app.route('/<string:name>/')
# def hello(name):
#     return "Hello " + name
# app.run()


# def function1():
#     print('hello')

# print("this out side of the function ")

# function1()
# 

# ------------------------------
# def func(y):
#     print(y + 4)
#     if y >= 10:
#         return(y+2)
#     else:
#         return(y+5)
    
# result = func(12)
# print(result)





# ----------------------------------
# name1 = "prageeth"
# height1 = 156
# weight1 = 80

# name2 = "Hovin"
# height2 = 102
# weight2 = 20

# name3 = "Anu"
# height3 = 152
# weight3 = 65

# def bmi_calculator(name, height, weight):
#     height_kg = height * 0.01
#     bmi = weight / height_kg ** 2
#     print("BMI results: ")
#     if bmi < 25 : 
#         return name + " is not over weight, BMI value is : " + str(bmi)
#     else: 
#         return name + " is over weight, BMI value is :  " + str(bmi)


# print (bmi_calculator(name1, height1, weight1))

# -------------------------------------------

# def fun2(name):
#     ab = name + 2
#     return ab
# aa= 5
# print(fun2(aa))
# -------------------------------------------


# num1 = 10

# def func1(num1):
#     if num1<10:
#         print("*" * num1)
#     else :
#         print("@" * num1)

# func1(5)    




book_db = {
    1 : {"name" : "pk" , "date" : "Jan 2021"},
    2 : {"name" : "kl" , "date" : "feb 2021"},
    3 : {"name" : "k2" , "date" : "feb 2021"},
    4 : {"name" : "kl3" , "date" : "feb 2021"}
}

book_db[5] = {"name" : "kl66" , "date" : "feb 2021"}

def readfunc(num):
    # print (book_db[name])
    name2 = book_db[num]
    return name2

def printall():
    for key, value in book_db.items() :
        print (key, value)
    print("TOT number of item is: " + str(len(book_db)))



def add_item(name, date):
    index = len(book_db) + 1
    book_db[index] = {"name" : name, "date" : date}
    return "Book added sucessfully!!"

def update_item(key, name, date):
    book_db[key] = {"name" : name, "date" : date}
    return "Book updated sucessfully!!"

def delete_item(key):
    book_db.pop(key)
    return "Book deleted sucessfully!!"



add_item("pr", "Mar 1980")
update_item(2,"pp","Nov 2021")
delete_item(1)
printall()

