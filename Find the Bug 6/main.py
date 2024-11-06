# Xavier Raty Find the Bug 6

# The function should return True if the number is between 10 and 20 (inclusive), but it doesn't. Find the bug.

def is_between(num):

     if num >= 10 and num <= 20:

          return True
     
     return False

print(is_between(10))