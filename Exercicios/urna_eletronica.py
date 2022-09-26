bolsonaro = 22
lula = 13

zema = 20
kalil = 30

president = [bolsonaro, lula]
governor = [zema, kalil]

count_zema = 0
count_kalil = 0
count_bolsonaro = 0
count_lula = 0

vote = 0
while vote == 0:
    vote_governor = int(input('Insert the governor: '))
    if vote_governor in governor:
        if vote_governor == 20:
            name_governor = 'Zema'
            fake_governor = 'Kalil'
            fake_vote_governor = 30
            count_kalil += 1
        else:
            name_governor = 'Kalil'
            count_kalil += 1
        print('Your vote is: {} ' .format(name_governor) + 'number ' + str(vote_governor))
        #print('Your vote is: ' + str(name_governor))
        confirm_governor = input('Do you confirm? (Y=yes or N=no)')
        y = 0
        while y == 0:
            if confirm_governor == 'Y' or 'y' in confirm_governor:
                vote_president = int(input('Insert the president: '))
                if vote_president in president:
                    if vote_president == 22:
                        name_president = 'Bolsonaro'
                        fake_president = 'Lula'
                        fake_vote_president = 13
                        count_lula += 1
                    else:
                        name_president = 'Lula'
                        count_lula += 1
                    print('Your vote is: {} ' .format(name_president) + 'number ' + str(vote_president))
                    #print('Your vote is: ' + str(name_president))
                    confirm_president = input('Do you confirm? (Y=yes or N=no)')
                    x = 0
                    while x == 0:
                        if confirm_president == 'Y' or 'y' in confirm_president:
                            x += 1
                            y += 1
                            vote += 1
                        else:
                            count_lula = 0
                            x += 1
                else:
                    print('Doesnt exist president!!!!')
            else:
                count_kalil = 0
                y += 1
    else:
        print('Doesnt exist governor!!!!')

print('\n')

print('Your vote for Governor is: {} '.format(name_governor) + str(vote_governor))
print('Your vote for President is: {} '.format(name_president) + str(vote_president) + '\n')

print('Total votes Bolsonaro: ' + str(count_bolsonaro))
print('Total votes Lula: ' + str(count_lula) + '\n')

print('Thanks to vote!!')