# Python create a quiz assignment

print("Welcome to the quiz")

# Score
score = 0

# Question 1
print("\n1. Who are the developers of the Half-Life series?")
answer1 = input("Q1 Answer: ").lower()
if answer1 == "valve" or answer1 == "captivation digital laboratories":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 2
print("\n2. Which sandbox game was initially made as a mod for Half-Life 2?")
answer2 = input("Q2 Answer: ").lower()
if answer2 == "gmod" or answer2 == "garry's mod":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 3
print("\n3. Which engine was Half-Life developed on?")
answer3 = input("Q3 Answer: ").lower()
if answer3 == "goldsrc" or answer3 == "gold source":
    print("Correct")
    score += 1
else:
    print("Incorrect")

# Question 4
print("\n4. Which first person shooter was released by Valve in 1998?")
answer4 = input("Q4 Answer: ").lower()
if answer4 == "half life" or answer4 == "half-life":
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
