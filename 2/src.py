import re


valid = 0
# with open('input.txt') as fh:
#     text = fh.readlines()

#     for line in text:
#         m = re.match(reg, line)
#         cnt = m.group(4).count(m.group(3))

#         if cnt < int(m.group(1)) or cnt > int(m.group(2)):
#             continue

#         valid += 1

reg = r"(\d\d?)-(\d\d?) ([a-z]): ([a-z]+)"
with open('input.txt') as fh:
    text = fh.readlines()

    for line in text:
        m = re.match(reg, line)
        x = m.group(4) + " " * 100
        i1 = x[int(m.group(1)) - 1]
        i2 = x[int(m.group(2)) - 1]

        if i1 == i2 == m.group(3) or (i1 != m.group(3) and i2 != m.group(3)):
            continue

        valid += 1

print(valid)
