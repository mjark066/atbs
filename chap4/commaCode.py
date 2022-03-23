def commaCode(list):
    if len(list) == 0:
        print('List is empty.')
    elif len(list) == 1:
        print('Only ' + list[0] + ' :(.')
    else:
        for i in range (0, len(list)):
            if i == (len(list) - 1):
                print('and ' + list[i] + '!')
            else:
                print(list[i], end=', ')


spam = ['apples']
commaCode(spam)