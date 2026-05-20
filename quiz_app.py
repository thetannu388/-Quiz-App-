print("Python Quiz")

score = 0

answer = input("Q1. Python kis type ki language hai? ")

if answer.lower() == "programming":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer = input("Q2. 5 + 5 = ")

if answer == "10":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("Your Score:", score)