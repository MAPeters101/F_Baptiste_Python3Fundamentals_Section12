squares = [i ** 2 for i in range(5)]
print(squares)
print(type(squares))
print()

squares = (i ** 2 for i in range(5))
print(squares)
print(type(squares))

for i in squares:
    print(i)
print('--')
for i in squares:
    print(i)
print('----')
squares = (i ** 2 for i in range(5))

for i in squares:
    print(i)

