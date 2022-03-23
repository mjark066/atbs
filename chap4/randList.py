### Revisit in the future ###
import random
n_streaks = 0
streak = 0
list_size = 100
for experimentNumber in range(10000):
    randList  = []
    for ii in range (list_size):
        value = random.randint(0,1)
        if value:
            randList.insert(ii, 'H')
        elif not value:
            randList.insert(ii, 'T')
    for kk in range (list_size):
        if  kk == 0:
            continue
        else:
            if randList[kk] == randList[kk - 1]:
                streak += 1
            else:
                streak = 0

        if streak == 6:
            n_streaks += 1
            streak = 0

print('The percentage is %s ' % (n_streaks / 100))


