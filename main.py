import random
import time
from score_utils import *
#usernames = ["Joseph", "Josh", "Jayden", "Adam", "Zack", "Robert", "Miss"]
#passwords = ["1234", "2345", "3456", "4567", "zack", "robert", "misspassword"]
usernames = []
passwords = []
round = 1
authenticated = False
p1score = 0
p2score = 0

user1 = ""
user2 = ""

highest_score = 0

with open("usernames.txt", 'r') as y:
    for x in y:
        usernames.append(x.strip())
with open("passwords.txt", 'r') as z:
    for x in z:
        passwords.append(x.strip())


def login():
    global usernames
    global passwords
    both_authenticated = False

    while both_authenticated == False:
        user1 = str(input("Enter Username 1: "))
        pass1 = str(input("Enter Password 1: "))
        user2 = str(input("Enter Username 2: "))
        pass2 = str(input("Enter Password 1: "))

        if user1 in usernames and user2 in usernames:
            if pass1 in passwords and pass2 in passwords:
                #check player 1
                u1index = usernames.index(user1)
                p1index = passwords.index(pass1)
                u2index = usernames.index(user2)
                p2index = passwords.index(pass2)
                if u1index == p1index and u2index == p2index:
                    both_authenticated = True
                else:
                    print("Incorrect passwords!")
            else:
                both_authenticated = False
                print("Details are incorrect!")
        else:
            both_authenticated = False
            print("Usernames not found")

    else:
        return True

def diceroll(pn):
    global p1score
    global p2score
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    print("Player " + str(pn) + " has rolled: " + str(d1) + " and " + str(d2))
    total = d1 + d2
    if total % 2 == 0:
        #even number
        total += 10
        if pn == 1:
            p1score += total
        else:
            p2score += total
    else:
        #odd number
        if pn == 1:
            p1score += total
            if p1score < 5:
                p1score = 0
            else:
                p1score = p1score - 5
        else:
            p2score += total
            if p2score < 5:
                p2score = 0
            else:
                p2score = p2score - 5
    

while authenticated == False:
    authenticated = login()
else:
    #start game
    print("Both users are authenticated, game will now start.")

    while round < 6:
        #game continues
        print("Player 1 will now roll: ")
        time.sleep(1)
        diceroll(1)
        time.sleep(1)
        print("Player 2 will now roll: ")
        diceroll(2)
        time.sleep(1)
        print("Player 1 Score: " + str(p1score))
        print("Player 2 Score: " + str(p2score))
        round += 1
        time.sleep(1)
    else:
        print("Game has ended!")
            
        if p1score == p2score:
            while p1score == p2score:
                diceroll(1)
                diceroll(2)
            else:
                print("Continue")
        else:
            print("Game has finished!")
            time.sleep(0.5)
            print("The scores are:")
            print("Player 2: " + str(p1score))
            print("Player 2: " + str(p2score))
            if p1score > p2score:
                print("Player 1 has won with, " + str(p1score) + " points.")
            else:
                print("Player 2 has won with, " + str(p2score) + " points.")
      
        # get and write scores
        outputScore(user1, user2, p1score, p2score, "score_n.txt", "score_a.txt")
        data = getHighestScore("score_n.txt", "score_a.txt")
        
        if data == "There is not a highest score yet!":
            print("There is currently no highest score")
        else:
            print("The Current Highest Score is: " + str(data[0]) + ":" + str(data[1]))


