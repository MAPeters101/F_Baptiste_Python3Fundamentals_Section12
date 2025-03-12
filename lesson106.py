l = [1,2,3]

iterator = iter(l)
print(type(iterator))
print(id(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))
#print(next(iterator))
print()

iterator = iter(l)
print(type(iterator))
print(id(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))
#print(next(iterator))
print('-'*80)


l = [1,2,3,4,5]
for element in l:
    print(element)
print()

# iterator = iter(l)
# while True:
#     element = next(iterator)
#     print(element)
# print()

iterator = iter(l)
try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    print('Done iterating...')
    pass
print()

iterator = iter(l)
try:
    while True:
        element = next(iterator)
        print(element)
except StopIteration:
    pass
print('-'*80)

r = range(10)
print(r)
r_iter = iter(r)
print(next(r_iter))
print(next(r_iter))
print(next(r_iter))
print(list(r_iter))
r = range(100_000_000)

for i in range(100_000_000):
    print(i)
    if i > 4:
        break
print('-'*80)


from time import perf_counter
start = perf_counter()
#l = range(100_000_000)
l = range(1_000_000)
end = perf_counter()
print(f'elapsed: {end - start}')

start = perf_counter()
#l = list(range(100_000_000))  This line crashed the computer
l = list(range(1_000_000))
end = perf_counter()
print(f'elapsed: {end - start}')
del l
print('-'*80)


r = range(10)
print(list(r))
print(list(r))
enum = enumerate('abc')
print(list(enum))
print(list(enum))
#print(next(enum))
print(list(enumerate('abc')))
print()

print(iter(enum) is enum)



