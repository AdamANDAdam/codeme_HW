# game
import random
import sys
k = int(input('Insert how many times you want to play'))
#def draw(figure):

def main():
    figure = ''
    for i in range(k):
        while True:

            figure = input('Type R - for the rock, P - for the paper, or S - for the scissors')
            if figure == 'S':
                draw(figure)
                break
            elif figure == 'R':
                draw(figure)
                break
            elif figure == 'P':
                draw(figure)
                break
            elif figure == 'End':
                sys.exit()
            else:
                print('Type R or S or P only, try again')


def draw(figure):
    win_counter = 0
    lose_counter = 0
    drawn = random.randint(1, 99)
    if drawn <= 33:
        drawn = 'P'
    elif 33 < drawn <= 66:
        drawn = 'R'
    else:
        drawn = 'S'

    for i in range(k):
        if figure == drawn:
            print('Draw')
        elif figure == 'R' and drawn == 'S':
            print('You won')
            win_counter += 1
        elif figure == 'S' and drawn == 'P':
            print('You lost')
            lose_counter += 1
        elif figure == 'P' and drawn == 'S':
            print('You lost')
            lose_counter += 1
        elif figure == 'S' and drawn == 'R':
            print('You lost')
            lose_counter += 1
        elif figure == 'R' and drawn == 'P':
            print('You won')
            win_counter += 1
    print(win_counter, lose_counter)

main()