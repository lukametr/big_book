import random

input('Press Enter to begin')

p1Name = input('Human player 1, enter your name: ')
p2Name = input('Human player 2, enter your name: ')
playerNames = p1Name[:11].center(11) + '   ' + p2Name[:11].center(11)

print('''HERE ARE TWO BOXES:
:
    __________    __________
   /         /|  /         /|
  +---------+ | +---------+ |
  |   RED   | | |   GOLD  | |
  |   BOX   | / |   BOX   | /
  +---------+/  +---------+/''')

print()
print(playerNames)
print()
print(p1Name + ', you have a RED box in front of you.')
print(p2Name + ', you have a GOLD box in front of you.')
print()
print(p1Name + ', you will get to look into box.')
print(p2Name.upper() + ', close your eyes and don\'t look!')
input('Wnen ' + p2Name + ' has closed their eyes, press Enter')
print()

print(p1Name + ', here is the inside of your box:')

if random.randint(1, 2) == 1:
    carrotInBox = True
else:
    carrotInBox = False

if carrotInBox:
    print('''
     ____W____
    |    W    |
    |    W    |
    |   ||    |
    ____||____    __________
   /         /|  /         /|
  +---------+ | +---------+ |
  |   RED   | | |   GOLD  | |
  |   BOX   | / |   BOX   | /
  +---------+/  +---------+/
   (cerrot!)''')
    print(playerNames)
else:
    print('''
     _________
    |         |
    |         |
    |_________|    _________
   /         /|  /         /|
  +---------+ | +---------+ |
  |   RED   | | |   GOLD  | |
  |   BOX   | / |   BOX   | /
  +---------+/  +---------+/
  (no carrot!)''')
    print(playerNames)

input('Press Enter to continue.')

print('\n' * 100)
print(p1Name + ', tell ' + p2Name + ' to open their eyes.')
input('Press Enter to continue.')

print()
print(p1Name + ', say one of the following sentences to ' + p2Name + '.')
print(' 1) There is a carrot in my box.')
print(' 2) There is not a carrot in my box.')
print()
input('Then press Enter to continue...')

print()
print(p2Name + ', do you want to swap boxes with ' + p1Name + '? YES/NO')
while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(p2Name + ', Please enter "YES" or "NO".')
    else:
        break

firstBox = 'RED'
secondBox = 'GOLD'

if response.startswith('Y'):
    carrotInFirstBox = not carrotInBox
    firstBox, secondBox = secondBox, firstBox

print('''HERE ARE THE TWO BOXES:
    __________    __________
   /         /|  /         /|
  +---------+ | +---------+ |
  |   RED   | | |   GOLD  | |
  |   BOX   | / |   BOX   | /
  +---------+/  +---------+/'''.format(firstBox, secondBox))
print(playerNames)

input('Press Enter to reveal the winner.')
print()

if carrotInFirstBox:
    print('''
     ____W____
    |    W    |
    |    W    |
    |   ||    |
    ____||____    __________
   /         /|  /         /|
  +---------+ | +---------+ |
  |   {}    | | |   {}    | |
  |   BOX   | / |   BOX   | /
  +---------+/  +---------+/'''.format(firstBox, secondBox))

else:
    print('''
                     ____W____
                    |    W    |
                    |    W    |
                    |   ||    |
      __________    __________
     /         /|  /         /|
    +---------+ | +---------+ |
    |   {}    | | |   {}    | |
    |   BOX   | / |   BOX   | /
    +---------+/  +---------+/'''.format(firstBox, secondBox))

    print(playerNames)

    if carrotInFirstBox:
        print(p1Name + ' is the winner!')
    else:
        print(p2Name + ' is the winner!')

    print('Thanks for playing!')