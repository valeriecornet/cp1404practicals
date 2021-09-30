"""Quick Pick Lottery Ticket Generator"""
import random
ROWS = 6
MIN_NUM = 1
MAX_NUM = 45

quick_picks = int(input("How many quick picks? "))
for i in range(quick_picks):
    quick_pick = []
    for number in range(ROWS):
        number = random.randint(MIN_NUM, MAX_NUM)
        while number in quick_pick:
            number = random.randint(MIN_NUM, MAX_NUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join("{}".format(number) for number in quick_pick))
