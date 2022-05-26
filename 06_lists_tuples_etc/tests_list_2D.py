# you can modify a list
cols = 50
rows = 50
listA = [[0]*2]*2
print(listA)

# you cannot modify tuple! change it back to list and then modify and back to tuple
tuple1 = (1,2, 'A', 4)
print(tuple1)

user = ('Jan', 'Kowalski', 1990)
(name, surname, DOB) = user
print(name, surname, DOB)

# sets are unique and disordered
set1 = set('qwert')
print(set1)

