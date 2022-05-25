# task 02

def inputs(Sum1):
    if Sum1 >= 100:
        print(f'Results is {Sum1}')
    else:
        print(f'Ens')

def main():
    no1 = int(input('Insert first number'))
    no2 = int(input('Insert second number'))
    Sum1 = no1+no2
    inputs(Sum1)
main()