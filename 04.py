# Day 4
# https://adventofcode.com/2022/day/4

data = """4-90,1-4
80-94,80-81
1-97,96-99
20-87,20-88
84-84,83-88
9-75,10-75
7-25,24-48
10-99,11-98
4-98,1-1"""

data = open('/tmp/data').readlines()

def fully_contain(l1, l2):
    # Return True if any one list in current order fully contains the other
    check1 = all(item in l1 for item in l2)
    check2 = all(item in l2 for item in l1)
    return any((check1, check2))

sum = 0
for line in data:
    line = line.strip().split(',')
    pair = list()
    for alloc in line:
        r1 = int(alloc.split('-')[0])
        r2 = int(alloc.split('-')[1])+1
        pair.append(range(r1, r2))
    if fully_contain(*pair):
        sum += 1

print(sum)

# Part 2
def partially_contain(l1, l2):
    # Return True if any one list in current order partially contains the other
    check1 = any(item in l1 for item in l2)
    check2 = any(item in l2 for item in l1)
    return any((check1, check2))

sum = 0
for line in data:
    line = line.strip().split(',')
    pair = list()
    for alloc in line:
        r1 = int(alloc.split('-')[0])
        r2 = int(alloc.split('-')[1])+1
        pair.append(range(r1, r2))
    if partially_contain(*pair):
        sum += 1

print(sum)

