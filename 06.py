# Advent day 6

data = open('/tmp/data').read()

from collections import deque

def get_start_msg(marker_len=4):
    dq = deque(maxlen=marker_len)
    counter = 0
    for byte in data:
        counter += 1
        dq.append(byte)
        if len(set(dq)) == marker_len:
            return (counter, dq)

counter, chars = get_start_msg()


#Part2
counter, chars = get_start_msg(14)


