import itertools
import multiprocessing as mp

def isValid0(l):
    return sum(l[0:3]) == 38 and sum(l[3:7]) == 38 and sum(l[7:12]) == 38 and sum(l[12:16]) == 38 and sum(l[16:19]) == 38

def rotate(it, indices):
    return map(lambda index: it[index], indices)

rotation1 = [2, 6, 11, 1, 5, 10, 15, 0, 4, 9, 14, 18, 3, 8, 13, 17, 7, 12, 16]
rotation2 = [11, 15, 18, 6, 10, 14, 17, 2, 5, 9, 13, 16, 1, 4, 8, 12, 0, 3, 7]

def isValid(l):
    return isValid0(l) and isValid0(rotate(l, rotation1)) and isValid0(rotate(l, rotation2))

def validOrEmpty(l):
    if isValid(l):
        return l
    else:
        return []

numbers = range(1, 20)

# print(list(rotate(numbers, rotation1)))
# print(list(rotate(numbers, rotation2)))

result = next(filter(isValid, itertools.permutations(numbers)))
print(result)

# if __name__ == '__main__':
#     with mp.Pool(mp.cpu_count()) as pool:
#         result = pool.map(validOrEmpty, itertools.permutations(numbers))
#         print(list(filter(lambda l: len(l) > 0, result)))
