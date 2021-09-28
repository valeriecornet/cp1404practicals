"""Ask user for score and return the result"""


def main():
    score = float(input("Enter score: "))
    result = calculate_status(score)
    print(result)


def calculate_status(score):
    if 100 < score < 0:
        print("Invalid score")
    else:
        if 0 > score > 100:
            print("Invalid score")
        elif score >= 50:
            print("Passable")
        elif score >= 90:
            print("Excellent")
        elif score < 50:
            print("Bad")


main()
