import random
import sys

draw = random.randint(1,100)
#print(draw)

for i in range(1,6):
        draw_player = int(input('Enter your random number 0 to 100'))
        if draw_player == draw:
            print('You won!')
            sys.exit()
        elif draw_player < draw:
            print("Bigger number")
        elif draw_player > draw:
            print("Smaller number")
print('You lost')