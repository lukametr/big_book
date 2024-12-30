import sys
import time
import sevseg

secondsLeft = 10
minutesLeft = 0
hoursLeft = 12  # Start at 12:00:00

try:
    while True:
        print('\n' * 60)

        hours = str(hoursLeft)
        minutes = str(minutesLeft)
        seconds = str(secondsLeft)

        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        print(hTopRow + '   ' + mTopRow + '   ' + sTopRow)
        print(hMiddleRow + ' * ' + mMiddleRow + ' * ' + sMiddleRow)
        print(hBottomRow + ' * ' + mBottomRow + ' * ' + sBottomRow)

        if secondsLeft == 0:
            secondsLeft = 59  # Reset to 59 seconds
            minutesLeft -= 1

        if minutesLeft < 0:
            minutesLeft = 59  # Reset to 59 minutes
            hoursLeft -= 1

        if hoursLeft < 0:
            break

        print()
        print('Press Ctrl-C to quit.')

        time.sleep(1)
        secondsLeft -= 1

except KeyboardInterrupt:
    sys.exit()