#!/usr/bin/env python3

import itertools
import multiprocessing as mp

def highlight(s):
    print('\x1b[6;30;42m' + str(s) + '\x1b[0m')

def sum38(it):
    return filter(lambda l: sum(l) == 38, it)

def candidates3(base, it):
    b0, b1, b2 = base
    filteredB0 = filter(lambda el: b0 != el[0] and b0 != el[1], it)
    filteredB1 = filter(lambda el: b1 != el[0] and b1 != el[1] and b1 != el[2], filteredB0)
    filteredB2 = filter(lambda el: b2 != el[1] and b2 != el[2], filteredB1)
    return filteredB2

def nextCandidates3(base, it):
    return filter(lambda el: base[2] == el[0], it)

def collectSuites3(result, candidate, remainingElements, headCandidates):
    if len(candidate) > 6:
        return
    if not(remainingElements) or not(headCandidates):
        if len(candidate) == 6 and candidate[0][0] == candidate[5][2]:
            result += [candidate]
        return

    for head in headCandidates:
        filteredHead = list(candidates3(head, remainingElements))
        nextHeadCandidates = list(nextCandidates3(head, filteredHead))
        collectSuites3(result, candidate + [head], filteredHead, nextHeadCandidates)

def isValid0(l):
    return sum(l[0:3]) == 38 and sum(l[3:7]) == 38 and sum(l[7:12]) == 38 and sum(l[12:16]) == 38 and sum(l[16:19]) == 38

def rotate(it, indices):
    return list(map(lambda index: it[index], indices))

rotation1 = [2, 6, 11, 1, 5, 10, 15, 0, 4, 9, 14, 18, 3, 8, 13, 17, 7, 12, 16]
rotation2 = [11, 15, 18, 6, 10, 14, 17, 2, 5, 9, 13, 16, 1, 4, 8, 12, 0, 3, 7]

def isValid(l):
    return isValid0(l) and isValid0(rotate(l, rotation1)) and isValid0(rotate(l, rotation2))

indicesOuter = [0, 1, 2, 6, 11, 15, 18, 17, 16, 12, 7, 3]
indicesInner = [4, 5, 8, 9, 10, 13, 14]

def collectResults(len3Candidate):
    result = []
    candidate = [0] * 19

    outerNumbers = list(itertools.chain.from_iterable(map(lambda l: l[:2], len3Candidate)))
    # TODO: duplication of numbers = range(1, 20)
    innerNumbers = set(range(1, 20)) - set(outerNumbers)

    for i in range(len(indicesOuter)):
        candidate[indicesOuter[i]] = outerNumbers[i]

    for p in map(list, itertools.permutations(innerNumbers)):
        for i in range(len(innerNumbers)):
            candidate[indicesInner[i]] = p[i]

        if isValid(candidate):
            result += candidate

    return result


if __name__ == '__main__':
    numbers = range(1, 20)

    len3 = map(list, itertools.permutations(numbers, 3))
    len3sum38 = list(sum38(len3))

    len3Candidates = []
    collectSuites3(len3Candidates, [], len3sum38, len3sum38)

    with mp.Pool(mp.cpu_count()) as p:
        result = list(filter(lambda r: len(r) > 0, p.map(collectResults, len3Candidates)))
        for r in result:
            highlight(r)
