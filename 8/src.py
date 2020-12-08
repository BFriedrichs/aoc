
raw = open('input.txt').read().splitlines()
inst = [(i, x[:3], int(x[4:])) for i, x in enumerate(raw)]

def compute(stack):
    visited = []
    acc = 0
    cp = 0
    did_finish = False
    while not did_finish:
        if cp >= len(stack):
            did_finish = True
            break
        (i, cmd, val) = stack[cp]
        if i in visited:
            break
        visited.append(i)
        if cmd == 'acc':
            acc += val
        elif cmd == 'jmp':
            cp += val
            continue
        cp += 1
    return acc, cp, did_finish

def part1():
    print(compute(inst))


def part2():
    for (i, cmd, val) in inst:
        copy = [i for i in inst]
        if cmd == 'jmp':
            copy[i] = (i, 'nop', val)
        elif cmd == 'nop':
            copy[i] = (i, 'jmp', val)
        else:
            continue
        acc, cp, did_finish = compute(copy)
        if did_finish:
            print(acc)
            return

# part1()
part2()