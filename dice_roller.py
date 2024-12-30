# ჩემთვის გაუგებარი მრავალკუთხოვანი კამათლის პროგრამა

import sys, random

while True:
    try:
        diceStr = input('> ')
        if diceStr.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        diceStr = diceStr.lower().replace(' ', '')
        dIndex = diceStr.find('d')
        if dIndex == -1:
            raise Exception('Missing the "d" character.')
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception('Missing the number of dice.')
        numberOfDice = int(numberOfDice)
        modIndex = diceStr.find('+')
        if modIndex == -1:
            modIndex = diceStr.find('-')
        if modIndex == -1:
            numberOfSides = diceStr[dIndex + 1 :]
        else:
            numberOfSides = diceStr[dIndex + 1 : modIndex]
        if not numberOfSides.isdecimal():
            raise Exception('Missing the number of sides.')
        numberOfSides = int(numberOfSides)

        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = int(diceStr[modIndex + 1 :])
            if diceStr[modIndex] == '-':
                modAmount = modAmount

        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(', '.join(rolls), end='')

        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(', {}{}'.format(modSign, abs(modAmount)), end='')
        print(')')

    except Exception as exc:
        print('Invalid inpyt. Enter something like "3d6" or "1d10+2".')
        print('Input was invalid because: ' + str(exc))
        continue


