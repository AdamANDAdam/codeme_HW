# factorial on loops

number = int(input('Insert a natural number from 1 to 8'))
if number == 0:
    print('0 is not a natural number')
for i in range(1, number+1):
    print(f'Factorial of {i} is equal to: {i*i}')




