# Python create a quiz assignment

print("Welcome to the quiz")

# Score
score = 0

# Question 1
print("\n1. Question")
answer1 = input("Q1 Answer: ").toLower()
if answer1 == "placeholder":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 2
print("\n2. Question")
answer2 = input("Q2 Answer: ").toLower()
if answer2 == "placeholder":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 3
print("\n3. Question")
answer3 = input("Q3 Answer: ").toLower()
if answer3 == "placeholder":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 4
print("\n4. Question")
answer4 = input("Q4 Answer: ").toLower()
if answer4 == "placeholder":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Output Result of Quiz
print("\nYour score is: " + str(score) +
      " / 4 " + str((score / 4) * 100) + "%")

if score == 4:
    print("Awesome!")
elif score == 3:
    print("Good Job")
elif score == 2:
    print("Okay")
elif score == 1:
    print("Try Again?")
else:
    print(":-/")
