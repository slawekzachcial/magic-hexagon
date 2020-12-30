import itertools
import multiprocessing as mp

def highlight(s):
    print('\x1b[6;30;42m' + str(s) + '\x1b[0m')

def sum38(it):
    return filter(lambda l: sum(l) == 38, it)

def ilen(it):
    return sum(1 for _ in it)

def candidates3(base, it):
    b0, b1, b2 = base
    filteredB0 = filter(lambda el: b0 != el[0] and b0 != el[1], it)
    filteredB1 = filter(lambda el: b1 != el[0] and b1 != el[1] and b1 != el[2], filteredB0)
    filteredB2 = filter(lambda el: b2 != el[1] and b2 != el[2], filteredB1)
    return filteredB2

def nextCandidates3(base, it):
    return filter(lambda el: base[2] == el[0], it)

def findSuites3(remainingElements, head, length):
    if len(remainingElements) == 0 or length == 0:
        return []

    filteredHead = list(candidates3(head, remainingElements))
    nextHeadCandidates = list(nextCandidates3(head, filteredHead))

    if length == 6 and head == [3, 17, 18]:
        print(f"  head: {head}")
        print(f"  remainingElements: {remainingElements}")
        print(f"  filteredHead: {filteredHead}")
        print(f"  nextHeadCandidates: {nextHeadCandidates}")

    if len(nextHeadCandidates) == 0:
        return [head]

    return [head] + findSuites3(filteredHead, nextHeadCandidates[0], length - 1)

def tbd(result, candidate, remainingElements, headCandidates):
    if len(candidate) > 6:
        return
    if not(remainingElements) or not(headCandidates):
        # print(f'  candidate: {candidate}')
        if len(candidate) == 6 and candidate[0][0] == candidate[5][2]:
            # highlight(f'  valid: {candidate}')
            result += [candidate]
            # print(result)
        return

    for head in headCandidates:
        filteredHead = list(candidates3(head, remainingElements))
        nextHeadCandidates = list(nextCandidates3(head, filteredHead))
        # print(f"  head: {head}")
        # print(f"  remainingElements: {remainingElements}")
        # print(f"  filteredHead: {filteredHead}")
        # print(f"  nextHeadCandidates: {nextHeadCandidates}")
        tbd(result, candidate + [head], filteredHead, nextHeadCandidates)


def filterValid3(results):
    return filter(lambda r: len(r) == 6 and r[0][0] == r[5][2], results)

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
    # print(len3Candidate)
    candidate = [0] * 19

    outerNumbers = list(itertools.chain.from_iterable(map(lambda l: l[:2], len3Candidate)))
    # TODO: duplication of numbers = range(1, 20)
    innerNumbers = set(range(1, 20)) - set(outerNumbers)
    # print(f" {outerNumbers} + {innerNumbers}")

    for i in range(len(indicesOuter)):
        candidate[indicesOuter[i]] = outerNumbers[i]

    for p in map(list, itertools.permutations(innerNumbers)):
        # print(f"  {p}")
        for i in range(len(innerNumbers)):
            candidate[indicesInner[i]] = p[i]

        # print(f" {candidate}")
        if isValid(candidate):
            result += candidate
            # highlight(f'found: {candidate}')

    return result


if __name__ == '__main__':
    numbers = range(1, 20)

    len3 = map(list, itertools.permutations(numbers, 3))
    len3sum38 = list(sum38(len3))
    # for i in len3sum38:
    #     print(i)

    # len3Suites = list(map(lambda head: findSuites3(len3sum38, head, 6), len3sum38))
    # for i in len3Suites:
    #     print(i)
    # len3Candidates = list(filterValid3(len3Suites))
    len3Candidates = []
    tbd(len3Candidates, [], len3sum38, len3sum38)

    # for i in len3Candidates:
    #     print(i)

    # len3Candidate = len3Candidates[0]
    # print(len3Candidate)

    # for len3Candidate in len3Candidates:
    #     # print(len3Candidate)
    #     candidate = [0] * 19

    #     outerNumbers = list(itertools.chain.from_iterable(map(lambda l: l[:2], len3Candidate)))
    #     innerNumbers = set(numbers) - set(outerNumbers)
    #     # print(f" {outerNumbers} + {innerNumbers}")

    #     for i in range(len(indicesOuter)):
    #         candidate[indicesOuter[i]] = outerNumbers[i]

    #     for p in map(list, itertools.permutations(innerNumbers)):
    #         # print(f"  {p}")
    #         for i in range(len(innerNumbers)):
    #             candidate[indicesInner[i]] = p[i]

    #         # print(f" {candidate}")
    #         if isValid(candidate):
    #             highlight(f'found: {candidate}')

    with mp.Pool(mp.cpu_count()) as p:
        result = list(filter(lambda r: len(r) > 0, p.map(collectResults, len3Candidates)))
        for r in result:
            highlight(r)

# highlight(findSuites3(len3sum38, len3sum38[0], 6))

# print("3: " + str(len(len3sum38)))
# print(len3sum38)

# first = len3sum38[0]
# highlight("### " + str([first]))

# filteredFirst = list(candidates(first, len3sum38))
# print("filteredFirst: " + str(filteredFirst))

# secondCandidates = list(nextCandidates3(first, filteredFirst))
# print("secondCandidates: " + str(secondCandidates))

# second = secondCandidates[0]
# highlight("### " + str([first, second]))

# filteredSecond = list(candidates(second, filteredFirst))
# print("filteredSecond: " + str(filteredSecond))

# thirdCandidates = list(nextCandidates3(second, filteredSecond))
# print("thirdCandidates: " + str(thirdCandidates))

# third = thirdCandidates[0]
# highlight("### " + str([first, second, third]))

# filteredThird = list(candidates(third, filteredSecond))
# print("filteredThird: " + str(filteredThird))

# fourthCandidates = list(nextCandidates3(third, filteredThird))
# print("fourthCandidates: " + str(fourthCandidates))

# fourth = fourthCandidates[0]
# highlight("### " + str([first, second, third, fourth]))

# filteredFourth = list(candidates(fourth, filteredThird))
# print("filteredFourth: " + str(filteredFourth))

# fifthCandidates = list(nextCandidates3(fourth, filteredFourth))
# print("fifthCandidates: " + str(fifthCandidates))

# fifth = fifthCandidates[0]
# highlight("### " + str([first, second, third, fourth, fifth]))

# filteredFifth = list(candidates(fifth, filteredFourth))
# print("filteredFifth: " + str(filteredFifth))

# sixthCandidates = list(nextCandidates3(fifth, filteredFifth))
# print("sixthCandidates: " + str(sixthCandidates))


# len4 = itertools.permutations(numbers, 4)
# len4sum38 = sum38(len4)

# print("4: " + str(ilen(len4sum38)))

# len5 = itertools.permutations(numbers, 5)
# len5sum38 = sum38(len5)

# print("5: " + str(ilen(len5sum38)))
