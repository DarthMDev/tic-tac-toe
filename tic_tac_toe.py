import random
"""
the game board
"""
print 'choose multiplayer or single player'
selectmode = raw_input(" Choose game mode :   ")

if selectmode == 'single player':
    print "You are X your goal is to win 3 in a row against the computer."
elif selectmode == 'multiplayer':
    print "You will be playing against your friend see who can win."

board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]

def checkLine(char, spot1, spot2, spot3):
    if board[spot1] == char and board[spot2] == char and board[spot3] == char:
        return True

def checkAll(char):
    if checkLine(char, 0, 1, 2):
        return True

    if checkLine(char, 1, 4, 7):
        return True
    if checkLine(char, 3, 4, 5):
        return True
    if checkLine(char, 6, 7, 8):
        return True
    if checkLine(char, 0, 3, 6):
        return True
    if checkLine(char, 0, 4, 8):
        return True
    if checkLine(char, 2, 4, 6):
        return True
    if checkLine(char, 2, 5, 8):
        return True

def show():
    print board[0], '|', board[1], '|', board[2]
    print '----------'
    print board[3], '|', board[4], '|', board[5]
    print '----------'
    print board[6], '|', board[7], '|', board[8]
show()
def multiplayer():
    while True:
        input = raw_input('Player 1 select a spot: ')
        input = int(input)
        if board[input] != 'x' and board[input] != 'o':
            board[input] = 'x'
            show()
#check
            if checkAll('x') == True:
                print "Player 1 wins!"
                break

        while True:
            secondinput = raw_input("Player 2 select a spot: ")
            secondinput = int(secondinput)
            if board[secondinput] != 'x' and board[secondinput] != 'o':
                board[secondinput] = 'o'
                if checkAll('o') == True:
                    print "Player 2 wins!"
                    break
                break
        else:
            print "This spot is taken!"
        show()


def single_player():
    while True:
        Input = raw_input("Select a spot: ")
        Input = int(Input)
        if board[Input] != 'x' and board[Input] != 'o':
            board[Input] = 'x'
#Check
            if checkAll('x') == True:
                print "X WINS!"
                break


        while True:
            random.seed() #give a random generator
            opponent = random.randint(0, 8)
            if board[opponent] != 'o' and board[opponent] != 'x':
            	board[opponent] = 'o'

#Check
            	if checkAll('o') == True:
                    print 'O WINS!'
                    break
                break

        else:
            print "This spot is taken!"
        show()
if selectmode == 'single player':
    while True:
        single_player()
        #if win == True:
        #    askplayagain = raw_input('Want to play again? Enter y for yes or n for no.')

        #playagain()
        break
elif selectmode == 'multiplayer':
    while True:
        multiplayer()
        break
