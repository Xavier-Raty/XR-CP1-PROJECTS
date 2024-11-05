# Xavier Raty What are these numbers

num1 = int(input("Give me a number you want converted to the thousands: "))
string = '{:,.2f}'.format(num1)
print(string)

num2 = int(input("Give me a number you want with 4 decial places: "))
string = '{:d}'.format(num2)
print(string)
