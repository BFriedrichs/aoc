import math

def get_range(search, start = 0, end = 127):
    diff = math.ceil((end - start) / 2)
    if search == '': return start
    elif search[0] in ['F', 'L']: return get_range(search[1:], start, end - diff)
    elif search[0] in ['B', 'R']: return get_range(search[1:], start + diff, end)


print(max([get_range(row[:7]) * 8 + get_range(row[7:], 0, 7) for row in open('input.txt').read().splitlines()]))

seats = [get_range(row[:7]) * 8 + get_range(row[7:], 0, 7) for row in open('input.txt').read().splitlines()]
for i in range(127 * 8):
    if i not in seats:
        print(i)