# Xavier Raty Graded Quiz
score = 0
question1 = int(input("What is 1+1?: "))
if question1 == 2:
    score += 1
question2 = int(input("What is 2x2?: "))
if question2 == 4:
    score += 1
question3 = int(input("What is 100/10?: "))
if question3 == 10:
    score += 1
question4 = int(input("What is 94-18?: "))
if question4 == 76:
    score += 1
question5 = int(input("What does 123-23+100x0 equal?: "))
if question5 == 0:
    score += 1

print(score)