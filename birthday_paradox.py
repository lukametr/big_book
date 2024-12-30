"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
 2. Explore the surprising probabilities of the "Birthday Paradox".
 3. More info at https://en.wikipedia.org/wiki/Birthday_problem
 4. View this code at https://nostarch.com/big-book-small-python-projects
 5. Tags: short, math, simulation"""

import datetime, random


def getBirthdays(numberOfBirthdays):

    birthdays = []
    for i in range(numberOfBirthdays):


        startOfYear = datetime.date(2001, 1, 1)


        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):


    if len(birthdays) == len(set(birthdays)):
        return None


    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return  birthdayA



print('''Birthday Paradox, by al@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It'd not actually a paradox, it's just a surprising result.)
''')

# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall i generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()


print('Here are', numBDays, 'birthdays')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:

        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()


match = getMatch(birthdays)


print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()


print('Generating', numBDays, 'ramdon birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 siulations.')
simMatch = 0
for i in range(100_000):

    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')


probability = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, 'people there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probability more than you would think!')

