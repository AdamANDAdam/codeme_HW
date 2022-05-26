nos = list(map(int, input("Input 10 numbers and split them by a space: ").split()))
nos_even = list(map(int, input("Input some numbers, total number of your numbers is even: ").split()))


# task 02 list

def odd_listing(nos):
    for i in nos:
        if i % 2 != 0:
            print(f"Odd number: {i}")

# task 04 list

def even_elements(nos_even):
    if len(nos_even) % 2 != 0:
       # print(f'Dlugosc: {len(nos_even)}')
        new_nos = nos_even.pop(len(nos_even)-1)
      #  print(f'Dlugosc new: {len(new_nos)}')
        index = int(len(new_nos)/2)
     #   print(index)
        print(f'Are the two mid numbers equal: {nos_even[int(index-1)] == nos_even[int(index+1)]}')
    else:
        index = int(len(nos_even)/2)
     #   print(f'Dlugosc: {len(nos_even)}')
     #   print(index)
        print(f'Are the two mid numbers equal: {nos_even[int(index-1)] == nos_even[int(index+1)]}')

odd_listing(nos)
even_elements(nos_even)