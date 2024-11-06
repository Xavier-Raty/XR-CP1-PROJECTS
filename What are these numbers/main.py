# Xavier Raty What are these numbers

num1 = int(input("Give me a number you want converted to the thousands: "))
string = '{:,.2f}'.format(num1)
print(string)

num2 = int(input("Give me a number you want with 4 decimal places: "))
string = '{:.4f}'.format(num2)
print(string)

num3 = int(input("Give me a number you want converted into a percentage: "))
string = '{:.2%}'.format(num3)
print(string)

num4 = int(input("Give me a number you want in a dollar amount: "))
string = '${:,.2f}'.format(num4)
print(string)