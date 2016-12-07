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

def x_is_about_to_win(spot1, spot2, spot3):
     if board[spot1] == 'x' and board[spot2] == 'x' and board[spot3] != 'o' and board[spot3] !='x':
         return True
def checkAlmostWin():
     if x_is_about_to_win(2,1,0):
         return 0
     if x_is_about_to_win(6,3,0):
         return 0
     if x_is_about_to_win(8,4,0):
         return 0
     if x_is_about_to_win(7,4,1):
         return 1
     if x_is_about_to_win(0,1,2):
         return 2
     if x_is_about_to_win(6,4,2):
         return 2
     if x_is_about_to_win(8,5,2):
         return 2
     if x_is_about_to_win(5,4,3):
         return 3
     if x_is_about_to_win(3,4,5):
         return 5
     if x_is_about_to_win(0,3,6):
         return 6
     if x_is_about_to_win(2,4,6):
         return 6
     if x_is_about_to_win(8,7,6):
         return 6
     if x_is_about_to_win(1,4,7):
         return 7
     if x_is_about_to_win(0,4,8):
         return 8
     if x_is_about_to_win(2,5,8):
         return 8
     if x_is_about_to_win(6,7,8):
         return 8

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
            if checkAlmostWin() == 0:
                opponent = 0
            elif checkAlmostWin() == 1:
                opponent = 1
            elif checkAlmostWin() == 2:
                opponent = 2
            elif checkAlmostWin() == 3:
                opponent = 3
            elif checkAlmostWin() == 4:
                opponent = 4
            elif checkAlmostWin() == 5:
                opponent = 5
            elif checkAlmostWin() == 6:
                opponent = 6
            elif checkAlmostWin() == 7:
                opponent = 7
            elif checkAlmostWin() == 8:
                opponent = 8
            else:
                random.seed()
                opponent = random.randint(0, 8)
            if board[opponent] != 'o' and board[opponent] != 'x':
            	board[opponent] = 'o'
#Check
            	if checkAll('o') == True:
                    print 'O WINS!'
                    break
                elif board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] !=4 and board[5]!= 5 and board[6] != 6 and board[7] != 7 and board[8] != 8 and checkAll('o') != True and checkAll('x') != True:
                    print 'Its a tie'
                    break
                break

        else:
            print "This spot is taken!"
        show()
if selectmode == 'single player':
    while True:
        single_player()
        askplayagain = raw_input('Want to play again? Enter y for yes or n for no.')
        if askplayagain.lower() == 'y':
            single_player()
        elif askplayagain.lower() == 'n':
            break
        break
elif selectmode == 'multiplayer':
    while True:
        multiplayer()
        askplayagain2 = raw_input('Want to play again? Enter y for yes or n for no.')
        if askplayagain2.lower() == 'y':
            multiplayer()
        elif askplayagain2.lower() == 'n':
            break
        break
