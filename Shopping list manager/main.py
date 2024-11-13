# Xavier Raty Shopping list manager

list = []

def add(item):
    list.append(item)
    print(list)

def remove(item):
    if item in list:
        where = list.index(item)
        list.pop(where)
        print(list)
    else:
        print("Item not found")
    
while True:

    action = input("""What would you like to do?

                                  Enter 1 to add item

                                  Enter 2 to remove item

                                  Enter 3 to leave the list:\n""")

    if action =="1":

        add(input("What do you want to add?: "))

    elif action =="2":

        remove(input("What do you want to remove?: "))

    else:

        print("Have a nice day!")

        break