# Xavier Raty Authorized

list = ["Joe", "Frank", "Bob", "Ms. LaRose", "Jeremy", "Emma", "El Taco", "Sus"]
list2 = ["Ms. LaRose", "Sus"]
x = input("What is your username? ")
if x in list:
    if x in list2:
        print("Hello Admin")
    else:
        print("Hello authorized user")
else:
    print("Your are not authorized")
