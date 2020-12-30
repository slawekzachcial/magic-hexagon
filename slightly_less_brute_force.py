#!/usr/bin/env python3

import itertools

def sum38(it):
    return filter(lambda l: sum(l) == 38, it)

def isValid0(l):
    return sum(l[0:3]) == 38 and sum(l[3:7]) == 38 and sum(l[7:12]) == 38 and sum(l[12:16]) == 38 and sum(l[16:19]) == 38

def rotate(it, indices):
    return map(lambda index: it[index], indices)

rotation1 = [2, 6, 11, 1, 5, 10, 15, 0, 4, 9, 14, 18, 3, 8, 13, 17, 7, 12, 16]
rotation2 = [11, 15, 18, 6, 10, 14, 17, 2, 5, 9, 13, 16, 1, 4, 8, 12, 0, 3, 7]

def isValid(l):
    return isValid0(l) and isValid0(list(rotate(l, rotation1))) and isValid0(list(rotate(l, rotation2)))


numbers = range(1, 20)

remaining0 = set(numbers)
for line0 in map(list, sum38(itertools.permutations(remaining0, 3))):
    remaining1 = remaining0 - set(line0)
    for line1 in map(list, sum38(itertools.permutations(remaining1, 4))):
        remaining2 = remaining1 - set(line1)
        for line2 in map(list, sum38(itertools.permutations(remaining2, 5))):
            remaining3 = remaining2 - set(line2)
            for line3 in map(list, sum38(itertools.permutations(remaining3, 4))):
                remaining4 = remaining3 - set(line3)
                for line4 in map(list, sum38(itertools.permutations(remaining4, 3))):
                    candidate = line0 + line1 + line2 + line3 + line4
                    if isValid(candidate):
                        print(candidate)
