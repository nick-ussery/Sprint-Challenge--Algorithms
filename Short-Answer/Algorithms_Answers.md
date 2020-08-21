#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)the condition of while loop is still O(n) and assigment of variable in loop is also negligible, the loop goes up by 3n, which is constant: 0(n)

b)nested loop in a for loop, worst case: O(n^2)

c)recursive linear, goes up same rate as input O(n)

## Exercise II

The best way would be to cut the options in half each step. Binary Search trees do this, so we would focus on finding the middle point, testing, then go down if egg breaks, up if egg survives.

find middle
throw egg at middle

if egg lives:
is len(arr) == 1? if so this is the highest floor allowed
if not recurse on high side
else:
recurse on low side

should be a 0(n) function. it is recursive, but it shears half the remaining options away at each decision
