__author__ = 'joel'
import random

print 'I am thinking of a 4-digit number. Try to guess what it is.'
print 'Here are some clues:'
print 'A state, the digit is correct and in the correct position.'
print 'B state, the digit is correct but in the wrong position.'
print 'When I say:  That means:'
print '2A1B         You get 3 digits are correct, and 2 of them is in the correct position.'
print 'You have 8 chances.'


def playAgain():
    print('Do you want to play again? (yes or no)')
    return raw_input().lower().startswith('y')


def generateSecretNum():
    secretNum = ''
    numberList = list(range(10))
    random.shuffle(numberList)
    for i in range(4):
        secretNum += str(numberList[i])
    return secretNum


def getGuess(chance):
    guessNum = ''
    while len(guessNum) != 4 or not isOnlyDigits(guessNum):
        print 'Guess #' + str(chance) + ':'
        guessNum = raw_input()

    return guessNum


def isOnlyDigits(num):
    if num == '':
        return False
    for i in num:
        if i not in '1 2 3 4 5 6 7 8 9 0'.split():
            return False
    return True

def getClue(guessNum, secretNum):
    A = 0
    B = 0
    for num in guessNum:
        if num in secretNum:
            B += 1
    for i in range(0, 4):
        if guessNum[i] == secretNum[i]:
            A += 1
    return [str(A), str(B-A)]


while True:
    print 'I am thinking of a 4-digit number. Try to guess what it is.'
    print 'You have 8 chances.'
    chance = 0
    secretNum = generateSecretNum()


    while chance <= 9:
        chance += 1

        if chance == 9:
            gameIsDone = True
            print 'You ran out of guesses. The answer was ' + secretNum
            break

        guessNum = getGuess(chance)

        if guessNum == secretNum:
            gameIsDone = True
            break

        clue = getClue(guessNum, secretNum)

        print 'Your guess is :  ' + guessNum
        print 'The result is :  ' + clue[0] + 'A' + clue[1] +'B'

    if gameIsDone:
        if playAgain():
            gameIsDone = False
        else:
            break



