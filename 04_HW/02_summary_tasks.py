name = (input('Insert some text'))
string_slicing = (input('Insert some text'))

odd = []
even = []

for i in range(len(name)):
    if i % 2 == 0:
        even.append(name[i])
    else:
        odd.append(name[i])

print(f'odd letters: {even}, and even letters: {odd}')

# string slicing method
print(string_slicing[0:len(string_slicing):2])
print(string_slicing[1:len(string_slicing):2])

