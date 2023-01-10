# Python create a quiz assignment

# Score
score = 0

# Question 1
answer1 = input("Who is your teacher? ")
if answer1 == "Mr. V" or answer1 == "Mr. Veldkamp":
    print("Correct")
    score += 1
else:
    print("Incorrect")


# Question 2
answer2 = input("What is 2 + 3")
if answer2 == "5":
    print("Correct")
    score += 1
else:
    print("Incorrect")
