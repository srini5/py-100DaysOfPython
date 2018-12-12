'''
This problem was asked by Facebook.
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

msg = 'Enter heights separated by commas (return key to exit): '
bounds = [int(x.strip()) for x in input(msg).split(',')]

total, buff, i, high, high2 = 0, 0, 0, 0, 0
bounded = False

prev = 0
for bound in bounds:
    curr = bound
    high = max(high,curr)

    if curr < high:
        high2 = max(high2, curr)

    if prev > 0 and curr > prev:
        bounded = True

    if curr < high:
        buff += (high - curr)
        i += 1
    else:
        total += buff
        buff = 0
        i = 0

    prev = curr

if bounded and buff > 0:
        total += (buff - i * (high - high2))

print('The total amount of water collected is: ', total)