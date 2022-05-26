import math

# HWs and re-done tasks
a = float(input('Enter side of your square:\n'))
# task 01
r = float(input('Enter your circle radius:\n'))
# task 02
number = float(input('Enter a positive integer (other numbers will be rounded):\n'))

nos = list(map(float, input("Input numbers and split them by a space: ").split()))

def square(a):
    """This function calculates the square area using sides value as parameter"""
    print(f'Your square is: {(a * a)}')


def circle_area(r):
    """This function computes your circle area"""
    print(f'Your circle area is approx.: {math.pi * r ** 2}')

def even(number):
    """This function tests the number even or odd"""
    if number % 2 != 0:
        print(f'You number {number} is odd.')
    else:
        print(f'You number {number} is even.')

def sum_of(nos):
    """This function takes a list of number and sums them all up"""
    print(f'The sum of all typed in numbers is {sum(nos)}')

def only_even(nos):
    for i in nos:
        if i % 2 == 0:
            print(f'This is an even number: {i}')
        else:
            print(f"This {i} number was not even")

square(a)
circle_area(r)
even(number)
sum_of(nos)
only_even(nos)
# print(square.__doc__)
