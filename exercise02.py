'''
Question 2
We saw in this section how generator expressions can be more efficient, not
only in terms os memory, but also in terms of computation time when not all
values in the generator are iterated.

Create a generator expression that when iterated over will produce the
integers from 1 to 10_000 raised to the power of 1, 2, 3, etc.

So this generator should produce these results:

1**1, 2**2, 3**3, 4**4, ...
Once you have created a generator expression to do this, time your results to
create the generator and iterate through the first 5 elements of the generator.

Then, do the same thing, but using a list comprehension instead of a generator
expression.

Hint: you should use the perf_counter apprioach we have seen a few times in
previous lectures:

from time import perf_counter

start = perf_counter()
# your code goes here
end = perf_counter()
print('elapsed:', end - start)
To make timings more accurate, you should time a loop that repeats your code
at least 10 times.
'''