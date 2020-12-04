
def c(inc_x, inc_y):
    x = 0
    y = 0
    while True:
        x += inc_x
        y += inc_y
        yield x, y

with open('input.txt') as fh:
    text = fh.read().splitlines()

    total = 1
    for incx, incy in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        cnt = 0
        for x, y in c(incx, incy):
            if y >= len(text):
                break
            r_x = x % len(text[y])

            if text[y][r_x] == '#':
                cnt += 1
        total *= cnt

    print(total)