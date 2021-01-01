#!/usr/bin/env python3

import sys
import itertools

HEXAGON_SIDES = 6

def isRingBaseCompatible(base, candidate):
    baseFirstMayOnlyBeLast = not(base[0] in candidate[0:-1])
    baseLastMayOnlyBeFirst = not(base[-1] in candidate[1:])
    baseMiddleMustBeNowhere = len(set(candidate) - set(base[1:-1])) == len(candidate)
    return baseFirstMayOnlyBeLast and baseLastMayOnlyBeFirst and baseMiddleMustBeNowhere

def isClosingRing(maybeRing):
    return maybeRing[0][0] == maybeRing[-1][-1]

def isNextCandidate(head, candidateSum, candidate):
    return head[-1] == candidate[0] and sum(candidate) == candidateSum

def collectRings(result, candidate, remaining, remainingSideSums, headCandidates):
    if len(candidate) > HEXAGON_SIDES:
        return
    if not(remaining) or not(headCandidates):
        if len(candidate) == HEXAGON_SIDES and isClosingRing(candidate):
            result += [candidate]
        return

    for head in headCandidates:
        nextHeadSum = remainingSideSums[0] if remainingSideSums else -1
        nextRemainingSideSums = remainingSideSums[1:] if remainingSideSums else []

        filteredHead = list(filter(lambda x: isRingBaseCompatible(head, x), remaining))
        nextHeadCandidates = list(filter(lambda x: isNextCandidate(head, nextHeadSum, x), filteredHead))
        collectRings(result, candidate + [head], filteredHead, nextRemainingSideSums, nextHeadCandidates)

def innerRingSums(outerRingSums, ring):
    return list(map(lambda i: outerRingSums[i] - ring[i-1][-2] - ring[(i+1) % HEXAGON_SIDES][1], range(HEXAGON_SIDES)))

def rings(sideSums, candidates):
    result = []
    collectRings(result, [], candidates, sideSums[1:],
                 list(filter(lambda l: sum(l) == sideSums[0], candidates)))

    return result

def ringToList(ring):
    return sum(map(lambda l: l[0:-1], ring), [])

def sideSize(cellCount):
    countCells = lambda n: 3*n*n-3*n+1
    n = next(x for x in itertools.count(1) if countCells(x) >= cellCount)
    if cellCount == countCells(n):
        return n
    raise ValueError(f'Unable to find n satisfying 3*n*n-3*n+1=={cellCount}')

def ringIndicesToLinear(ringList):
    ringLen = len(ringList)
    if ringLen == 1:
        return ringList
    # TODO: there must be a better way to do this!
    indicesForLength = {
        7: [0,1,5,6,2,4,3],
        19: [0,1,2,11,12,13,3,10,17,18,14,4,9,16,15,5,8,7,6],
        37: [0,1,2,3,17,18,19,20,4,16,29,30,31,21,5,15,28,35,36,32,22,6,14,27,34,33,23,7,13,26,25,24,8,12,11,10,9]
    }
    if ringLen in indicesForLength:
        return list(map(lambda i: ringList[i], indicesForLength[ringLen]))
    raise ValueError(f'Unable to remap indices for list of size {ringLen}')

def collectResults(results, current, sums, possibleNumbers, sideSize):
    if sideSize == 1:
        # if we get here - possibleNumbers is a 1-element set
        results += [current + list(possibleNumbers)]
        return

    possibleRings = rings(sums, list(filter(lambda x: sum(x) in sums,
                                            map(list, itertools.permutations(possibleNumbers, sideSize)))))

    for ring in possibleRings:
        ringNumbers = set(sum(ring, []))
        innerRingPossibleNumbers = possibleNumbers - ringNumbers
        innerSums = innerRingSums(sums, ring)

        collectResults(results, current + ringToList(ring), innerSums, innerRingPossibleNumbers, sideSize - 1)

if __name__ == '__main__':
    SIDE_SIZE = 3 if len(sys.argv) == 1 else int(sys.argv[1])
    SIDE_SUM = 38 if len(sys.argv) == 1 else int(sys.argv[2])
    rangeFrom = 1 if len(sys.argv) == 1 else int(sys.argv[3])
    rangeTo =  19 if len(sys.argv) == 1 else int(sys.argv[4])
    NUMBERS = range(rangeFrom, rangeTo+1)

    results = []

    outerRingSums = [SIDE_SUM] * HEXAGON_SIDES
    outerRingPossibleNumbers = set(NUMBERS)

    collectResults(results, [], outerRingSums, outerRingPossibleNumbers, SIDE_SIZE)

    for r in results: print(ringIndicesToLinear(r))
