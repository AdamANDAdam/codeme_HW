def dec_bin(number):
    if (number > 1):
        dec_bin(number//2)
    print(number%2, end='')
def bin_dec(bin_num):
   print(bin_num)

def main():
    number = int(input('Insert a decimal number (must be positive and integer greater than 1)'))
    dec_bin(number)
   # bin_num = str(input('Insert number i a binary form without a 0b prefix:'))
    bin_num = 0b1001111
    bin_dec(bin_num)

main()
# display numbers below in decimal system
# print('---------------------------')
# print(int(0x1DB), int(0o2063))
#
#
