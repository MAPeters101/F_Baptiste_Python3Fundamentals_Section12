'''
Question 1
Given the following list:

l = [10, 'abc', 3.14, True]
Write code that prints out the index number and value at that index for every element of l.

Solution
We could have do this by iterating the index numbers this way:

for i in range(len(l)):
    print(f'l[{i}] = {l[i]}')
l[0] = 10
l[1] = abc
l[2] = 3.14
l[3] = True
But a cleaner (and more "Pythonic") solution is to use the enumerate function:

for i, value in enumerate(l):
    print(f'l[{i}] = {value}')
l[0] = 10
l[1] = abc
l[2] = 3.14
l[3] = True
Question 2
We saw in this section how generator expressions can be more efficient, not only in terms os memory, but also in terms of computation time when not all values in the generator are iterated.

Create a generator expression that when iterated over will produce the integers from 1 to 10_000 raised to the power of 1, 2, 3, etc.

So this generator should produce these results:

1**1, 2**2, 3**3, 4**4, ...
Once you have created a generator expression to do this, time your results to create the generator and iterate through the first 5 elements of the generator.

Then, do the same thing, but using a list comprehension instead of a generator expression.

Hint: you should use the perf_counter apprioach we have seen a few times in previous lectures:

from time import perf_counter

start = perf_counter()
# your code goes here
end = perf_counter()
print('elapsed:', end - start)
To make timings more accurate, you should time a loop that repeats your code at least 10 times.

Solution
from time import perf_counter
Let's write the generator expression first:

g = (i ** i for i in range(1, 10_001))
Then we can iterate over the first five elements of the iterator:

for _ in range(5):
    print(next(g))
1
4
27
256
3125
We could also iterate over it this way:

g = (i ** i for i in range(1, 10_001))

for idx, value in enumerate(g):
    print(value)
    if idx == 4:
        break
1
4
27
256
3125
Now let's time this code repeated 10 times:

start = perf_counter()
for _ in range(10):
    g = (i ** i for i in range(1, 10_001))
    for _ in range(5):
        print(next(g))
end = perf_counter()
print('elapsed:', end - start)
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
elapsed: 0.00017687492072582245
Now let's do the same, but using a list comprehension - with a few minor modifications:

We can re-use the same list - unlike a generator which can only be used once - that will save some time
We can index a list for our iteration, a bit easier than the generator.
start = perf_counter()
l = [i ** i for i in range(1, 10_001)]
for _ in range(10):
    for value in l[:5]:
        print(value)
end = perf_counter()
print('elapsed:', end - start)
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
1
4
27
256
3125
elapsed: 5.784124583937228
'''