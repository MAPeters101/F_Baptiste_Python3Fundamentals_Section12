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
print('-'*80)

squares = (i ** 2 for i in range(5))
print(iter(squares) is squares)
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
#print(next(squares))
print('-'*80)

squares = (i ** 2 for i in range(5))
print(3 in squares)
#print(next(squares))
print(3 in [1,2,4])
print(list(squares))
squares = (i ** 2 for i in range(5))
print(list(squares))
print()
squares = (i ** 2 for i in range(5))
print(4 in squares)
print(4 in squares)
print(1 in squares)
print(9 in squares)
squares = (i ** 2 for i in range(5))
print(9 in squares)
print('-'*80)


squares = (i ** 2 for i in range(5))
print(4 in squares)
print(list(squares))
print('-'*80)



from timeit import timeit
print(timeit('[i**2 for i in range(25_000_000)]', number=1))
print(timeit('(i**2 for i in range(250_000_000_000))', number=1))




