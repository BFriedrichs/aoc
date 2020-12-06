
def part1(): print(sum([sum([chr(i) in g for i in range(97, 123) for g in row.replace('\n', '').split(' ')]) for row in open('input.txt').read().split('\n\n')]))
def part2():
    cnt = 0
    for g in open('input.txt').read().split('\n\n'):
        for c in set(g.replace('\n', '')):
            if all([c in p for p in g.replace('\n', ' ').split(' ')]):
                cnt += 1
    print(cnt)

part1()
part2()


