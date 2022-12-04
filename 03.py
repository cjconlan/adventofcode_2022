# Day 3
# https://adventofcode.com/2022/day/3

data = """dWlhclDHdFvDCCDfFq
mGdZBZBwRGjZMFgvTvgtvv
jwwJrzdzGdSbGGnNlzWczHzPHPhn
cczcbMBszhzzDBTBPPPGjtvtlt
LqJLfpwdLnvQLRGQjGtj
gSgnSJJCGSGpGSrwgfhchmmmHzcrHDmbrmMm
bVjstCsSstCLCrbSLnMpdMndcLddcqcpHR
wPZJQJwtBfJZmgBwPTcpTdcnfHMppcGMdG
gmFJzwPJJtszvNhCNC"""

data = open('/tmp/data', 'r').readlines()

def get_priority(char):
    if char.islower():
        return ord(char) - ord('a')+1
    return ord(char) - ord('A')+27

def get_char(str_input):
   # Get the common character between the ist and 2nd halves of a list
   idx = int(len(str_input)/2)
   for char in str_input[idx:]:
      if char in str_input[:idx]:
          return char

sum = 0
for line in data:
    common = get_char(line.strip())
    val = get_priority(common)
    sum += val

print(sum)


# Part 2
group_data = [data[n:n+3] for n in range(0, len(data), 3)]

def get_common(nested_list):
    # Get the common characters between lists
    for char in nested_list[0].strip():
        if all([char in sublist.strip() for sublist in nested_list[1:]]):
            return char
 
sum = 0
for group in group_data:
    char = get_common(group)
    sum += get_priority(char)

print(sum)
