#!/usr/bin/env python3

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

def sumsForRing(ring):
    return list(map(lambda i: ring[i-1][-2] + ring[(i+1) % HEXAGON_SIDES][1], range(HEXAGON_SIDES)))

def rings(sideSums, candidates):
    result = []
    collectRings(result, [], candidates, sideSums[1:],
                 list(filter(lambda l: sum(l) == sideSums[0], candidates)))

    return result

def ringToList(ring):
    return sum(map(lambda l: l[0:-1], ring), [])

def ringIndicesToLinear(ringList):
    if len(ringList) == 1:
        return ringList
    # TODO: there must be a better way to do this!
    if len(ringList) == 7:
        return list(map(lambda i: ringList[i], [0,1,5,6,2,4,3]))
    if len(ringList) == 19:
        return list(map(lambda i: ringList[i], [0,1,2,11,12,13,3,10,17,18,14,4,9,16,15,5,8,7,6]))
    return []

if __name__ == '__main__':
    SIDE_SIZE = 3
    SIDE_SUM = 38
    NUMBERS = range(1, 20)

    result = []

    outerRingSums = [SIDE_SUM] * HEXAGON_SIDES

    outerRings = rings(outerRingSums,
                       list(filter(lambda x: sum(x) in outerRingSums,
                                   map(list, itertools.permutations(NUMBERS, SIDE_SIZE)))))

    for outerRing in outerRings:
        outerRingNumbers = set(sum(outerRing, []))
        innerRingNumbers = set(NUMBERS) - outerRingNumbers
        innerRingSums = list(map(lambda v: SIDE_SUM - v, sumsForRing(outerRing)))

        innerRings = rings(innerRingSums,
                           list(filter(lambda x: sum(x) in innerRingSums,
                                       map(list, itertools.permutations(innerRingNumbers, SIDE_SIZE-1)))))

        for innerRing in innerRings:
            finalNumber = list(innerRingNumbers - set(sum(innerRing, [])))

            result += [ringToList(outerRing) + ringToList(innerRing) + finalNumber]


    for r in result: print(ringIndicesToLinear(r))
