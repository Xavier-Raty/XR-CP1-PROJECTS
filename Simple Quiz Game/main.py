# Xavier Raty Simple Quiz Game

score = 0

answer_1 = input("What is the Capital of the U.S? A) Washington D.C B) Salt Lake City C) San Fransisco D) Boston:")
if answer_1 == "A":
    score += 1
    print("Correct")
else: 
    print("Incorrect. The correct answer is A) Washington D.C.")
    print("We'll do an easier one next:")

answer_2 = input("How many states are in the U.S? A) 29 B) 93 C) 49 D) 50:")
if answer_2 == "D" :
    score += 1
    print("Correct")
else: print("Incorrect. The correct answer is D) 50")
      print("We'll do an easier one next:")

answer_3 = input("Select the major city that does not belong in the U.S: A) Salt Lake City B) Sacremento C) Singapore D) Boston:")
if answer_3 == "C" :
    score += 1
    print("Correct")
else: print("Incorrect. The correct answer is C) Singapore")
      print("We'll do an easier one next:")

answer_4 = input("Select the correct state that exists in the U.S: A) Lonma B) Vermont C) Ginger D) Minisoda:")
if answer_4 == "B" :
    score += 1
    print("Correct")
else: print("Incorrect. The correct answer is B) Vermont")
      print("We'll do an easier one next:")

answer_5 = input("Select the current president of the U.S A) George Washington B) Donald Trump C) Elon Musk D) Joe Biden:")
if answer_5 == "D" :
    score += 1
    print("Correct")
else: print("Incorrect. The correct answer is D) Joe Biden")
      print("We'll do an easier one next:")

print("This is your score:" score)
print("Thanks for playing!")
