# Advent 5
 
import os
import pandas as pd
 
data = open('/tmp/data', 'r').readlines()
 
 
def get_val(ldata, idx):
    # Try to get a value from a list, or return a space.
    try:
        return ldata[idx]
    except:
        return ' '
 
 
def show_stacks():
    # A function to print the stack at any time
    print()
    highest_stack = max([len(stacks[stack]['stack_items']) for stack in stacks])
    for idx in sorted(list(range(highest_stack)), reverse=True):
        for stack in stacks:
            print(get_val(stacks[stack]['stack_items'], idx), end='  ')
        print()  # next line
 
 
# Read data into two different sets
stack_data = list()
move_data = list()
prev_line = None
cols = None
dest_data = 'stack'
for line in data:
    line = line.replace(os.linesep, '')
    if not line and not cols:
        cols = prev_line
        dest_data = 'move'
        continue
    prev_line = line
    if dest_data == 'stack':
        stack_data.append(line)
    else:
        move_data.append(line)
 
stacks = {}
for idx, stack in enumerate(cols):
    # Remember the idx of where data is
    if stack.strip():
        stacks[stack] = {'col': idx, 'stack_items': []}
 
# Iterate the stack data, ignoring tha last 'stack count' line
for line in stack_data[:-1]:
    for stack in stacks:
        val = line[stacks[stack]['col']].strip()
        if val:
            stacks[stack]['stack_items'].insert(0, val)
 
show_stacks()
line_num = 0
for line in move_data:
    if not line: continue
    line_num += 1
    ser = pd.Series(line.split())
    indexes = [1, 3, 5]   # 'move 2 from 4 to 2'
    line_data = ser[indexes]
    qty, src, dst = line_data
    c = 0
    for _ in range(int(qty)):
        c +=1
        # Take from src stack and put in dst stack
        stacks[dst]['stack_items'].append(stacks[src]['stack_items'].pop())
 
 
res = ''.join((stacks[stack]['stack_items'][-1] for stack in stacks))
# CFFHVVHNC
