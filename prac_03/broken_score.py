"""Ask user for score and return the result"""

score = float(input("Enter score: "))
if 100 < score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    elif score >= 50:
        print("Passable")
    elif score >= 90:
        print("Excellent")
    elif score < 50:
        print("Bad")