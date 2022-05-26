# task 01

record = ('dog', 'Max', 'Shepherd')
(animal, name, race) = record
print(f'My pet is a {animal}, of a race {race}, and named {name}.')

# task 02

tuple_test = (1,2,3,4, 'A', 1, 1)
for i in tuple_test:
    print(tuple_test.count(i), i)

# task 03

nos = tuple(map(int, input("Input some numbers and split them by a space: ").split()))

for i in nos:
    print(nos.index(i),i)


