# Advent 01 - 2022

# $ cat > /tmp/data
# <paste list>
# CTRL-D

data = open('/tmp/data').readlines()
data = [val.strip() for val in data]
data.append('')

tmp = list()
grouped = list()
for amt in data:
    if amt:
       tmp.append(amt)
    else:
        grouped.add(tmp)
        tmp = list()

sorted_grouped_totals = sorted([sum(vals) for vals in grouped], reverse=True)
max_stash = sorted_grouped_totals[0]
max_stash

top_three_stash = sum(sorted_grouped_totals[0:3])
top_three_stash
