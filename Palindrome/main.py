# Xavier Raty Palindrome

word = input("Type a palindrome: ")
if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("This word isn't a palindrome")
