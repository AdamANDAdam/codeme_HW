# sort 3 numbrs

no1, no2, no3 = input('Enter 3 random numbers after comma').split(',')

inserted = [no1,no2,no3]
k = sorted(inserted)

print(f'Sorted numbers are: {k}, and biggest number is {max(no1,no2,no3)}')
