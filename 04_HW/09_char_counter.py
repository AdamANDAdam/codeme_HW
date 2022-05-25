# counter

my_str = input('Enter some string')

small_chars = 0
capital_chars = 0
digits = 0
special_chars = 0

for i in my_str:
    if i.isupper():
        capital_chars = capital_chars+1
    elif i.islower():
        small_chars = small_chars+1
    elif i.isdigit():
        digits = digits+1
    else:
        special_chars = special_chars+1

print(f'Small: {small_chars}, capital: {capital_chars}, digits {digits}, specials {special_chars}')
