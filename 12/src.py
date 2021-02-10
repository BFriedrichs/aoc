raw = open('input.txt').read().splitlines()

directions = ['N', 'E', 'S', 'W']
courses = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0), 'F': (1, 0)}
direction = 1
pos = [0, 0]

for move in raw:
    di = move[0]
    num = int(move[1:])

    if di == 'L':
        direction = (direction - num // 90) % 4
        courses['F'] = courses[directions[direction]]
    elif di == 'R':
        direction = (direction + num // 90) % 4
        courses['F'] = courses[directions[direction]]
    else:
        course = courses[di]
        pos[0] += course[0] * num
        pos[1] += course[1] * num

print(abs(pos[0]) + abs(pos[1]))
