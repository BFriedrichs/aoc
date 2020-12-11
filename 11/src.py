raw = open('input.txt').read().splitlines()

def direction_iter(down, right):
    x = y = 0
    while True:
        y += down
        x += right
        yield y, x

def count_neighbours(seats, i, j):
    count = 0
    for x in range(0, 9):
        yy = x // 3 - 1
        xx = x % 3 - 1
        if yy == 0 and xx == 0 or i+yy < 0 or j+xx < 0:
            continue
        # Who even needs proper index checking
        try:
            if seats[i+yy][j+xx] == '#':
                count += 1
        except:
            continue
    return count

def count_visible(seats, i, j):
    count = 0

    for x in range(0, 9):
        yy = x // 3 - 1
        xx = x % 3 - 1
        if yy == 0 and xx == 0:
            continue

        for sight_y, sight_x in direction_iter(yy, xx):
            if i+sight_y < 0 or j+sight_x < 0:
                break
            try:
                if seats[i+sight_y][j+sight_x] == 'L':
                    break
                elif seats[i+sight_y][j+sight_x] == '#':
                    count += 1
                    break
            except:
                break

    return count

def step(seats, needed=4, count_func=count_neighbours):
    new_seats = seats[:]
    did_change = False
    for i in range(len(seats)):
        for j in range(len(seats[i])):
            seat = seats[i][j]
            if seat == '.':
                continue
            else:
                count = count_func(seats, i, j)
                if seat == 'L' and count == 0:
                    new_seats[i] = new_seats[i][:j] + '#' + new_seats[i][j+1:]
                    did_change = True
                elif seat == '#' and count >= needed:
                    new_seats[i] = new_seats[i][:j] + 'L' + new_seats[i][j+1:]
                    did_change = True
    return new_seats, did_change

def part1():
    seats, did_change = step(raw)
    while did_change:
        seats, did_change = step(seats)
    occupied = ''.join(seats).count('#')
    print(occupied)


def part2():
    seats, did_change = step(raw, 5, count_visible)
    while did_change:
        seats, did_change = step(seats, 5, count_visible)
    occupied = ''.join(seats).count('#')
    print(occupied)

# part1()
part2()