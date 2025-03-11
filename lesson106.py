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
print()

