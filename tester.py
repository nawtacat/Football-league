import random
import math
import time


def main():
    while True:
        teams = ["PSG", "Barcelona", "Manchester City", "Bayern Munich"]
        nomore = ["PSG", "Barcelona", "Manchester City", "Bayern Munich"]
        group = []
        index1 = random.randint(0, 3)
        group.append(nomore[index1])
        del nomore[index1]
        index2 = random.randint(0, 2)
        group.append(nomore[index2])
        del nomore[index2]
        pair1 = nomore
        pair2 = group

        print("First Group")
        print(group[0] + " v " + group[1])
        print("Second Group")
        print(nomore[0] + " v " + nomore[1])

        psg_rate = 9
        barca_rate = 7
        mnc_rate = 10
        bayern_rate = 6

        score = 100

        rates = {
            "PSG": psg_rate,
            "Barcelona": barca_rate,
            "Manchester City": mnc_rate,
            "Bayern Munich": bayern_rate
        }

        print(' ')
        print("The League has been Started")
        print("You have an initial 100 Dollars")
        choice1 = input("Who is the Winner " + pair1[0] + " or " + pair1[1] + "?: ")
        bet = int(input("How Many Percent in? (10 - 90): "))
        print(" ")
        print("Ok, The Game is on, Please Wait")
        time.sleep(4)
        winner1 = random.randint(1, rates[pair1[0]] + rates[pair1[1]])
        print(" ")
        if winner1 < rates[pair1[0]] + 1 and choice1 == pair1[0]:
            print("Congrats " + pair1[0] + " Won and So Did You")
            score = math.floor(score + score * bet/100)
            print("You have " + str(score) + " Dollars")
            win1 = pair1[0]
        elif winner1 > rates[pair1[0]] and choice1 == pair1[1]:
            print("Congrats " + pair1[1] + " Won and So Did You")
            score = math.floor(score + score * bet / 100)
            print("You have " + str(score) + " Dollars")
            win1 = pair1[1]
        elif winner1 > rates[pair1[0]] and choice1 == pair1[0]:
            print("Oops " + pair1[1] + " Won, You Lost")
            score = math.floor(score - score * bet / 100)
            print("You have " + str(score) + " Dollars")
            win1 = pair1[1]
        elif winner1 < rates[pair1[0]] and choice1 == pair1[1]:
            print("Oops " + pair1[0] + " Won, You Lost")
            score = math.floor(score - score * bet / 100)
            print("You have " + str(score) + " Dollars")
            win1 = pair1[0]

        print(" ")
        choice2 = input("Who is the Winner " + pair2[0] + " or " + pair2[1] + "?: ")
        bet = int(input("How Many Percent in? (10 - 90): "))
        print(" ")
        print("Ok, The Game is on, Please Wait")
        time.sleep(4)
        winner2 = random.randint(1, rates[pair2[0]] + rates[pair2[1]])
        print(" ")
        if winner2 < rates[pair2[0]] + 1 and choice2 == pair2[0]:
            print("Congrats " + pair2[0] + " Won and So Did You")
            score = math.floor(score + score * bet / 100)
            print("You have " + str(score) + " Dollars")
            win2 = pair2[0]
        elif winner2 > rates[pair2[0]] and choice2 == pair2[1]:
            print("Congrats " + pair2[1] + " Won and So Did You")
            score = math.floor(score + score * bet / 100)
            print("You have " + str(score) + " Dollars")
            win2 = pair2[1]
        elif winner2 > rates[pair2[0]] and choice2 == pair2[0]:
            print("Oops " + pair2[1] + " Won, You Lost")
            score = math.floor(score - score * bet / 100)
            print("You have " + str(score) + " Dollars")
            win2 = pair2[1]
        elif winner2 < rates[pair2[0]] and choice2 == pair2[1]:
            print("Oops " + pair2[0] + " Won, You Lost")
            score = math.floor(score - score * bet / 100)
            print("You have " + str(score) + " Dollars")
            win2 = pair2[0]
        print(" ")
        print("We are Ready for The FINAL")
        print("We have " + win1 + " and " + win2 + " in FINAL")
        fchoice = input("Who's Gonna Win " + win1 + " or " + win2 + " ")
        fbet = int(input("how many percent in?: "))
        print("Ok, the game is on, please wait")
        time.sleep(4)
        fwinner = random.randint(1, rates[win1] + rates[win2])
        if fwinner < rates[win1] + 1 and fchoice == win1:
            print("Congrats " + win1 + " is the CHAMPION, You Won")
            score = math.floor(score + score * fbet / 100)
            print("You have " + str(score) + " Dollars")
        if fwinner < rates[win1] + 1 and fchoice == win2:
            print("Oops " + win1 + " is the CHAMPION, You Lost")
            score = math.floor(score + score * fbet / 100)
            print("You have " + str(score) + " Dollars")
        if fwinner > rates[win1] and fchoice == win2:
            print("Congrats " + win2 + " is the CHAMPION, You Won")
            score = math.floor(score + score * fbet / 100)
            print("You have " + str(score) + " Dollars")
        if fwinner > rates[win1] and fchoice == win1:
            print("Oops " + win2 + " is the CHAMPION, You Lost")
            score = math.floor(score + score * fbet / 100)
            print("You have " + str(score) + " Dollars")

        print(" ")
        play_again = input("press 'P + ENTER' to play again, press 'q' to quit ").lower
        if play_again == "p":
            pass
        if play_again == 'q':
            quit()




main()
