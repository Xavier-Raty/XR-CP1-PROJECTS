# Xavier Raty Simple Quiz Game

score = 0

answer_1 = input("What is the Capital of the U.S? A) Washington D.C B) Salt Lake City C) San Fransisco D) Boston:")
if answer_1 == "A":
    score += 1
    print("Correct")
else: 
    print("Incorrect. The correct answer is A) Washington D.C.")
    print("We'll do an easier one next:")