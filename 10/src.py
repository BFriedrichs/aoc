raw = sorted([0] + [int(i) for i in open('input.txt').read().splitlines()])

def part1():
    diffs = [raw[i+1] - raw[i] for i in range(len(raw) - 1)]
    print(diffs.count(1) * (diffs.count(3) + 1))

def build_chain(to_check, current=0, curr_chain=[]):
    num = to_check[current]
    new_chain = curr_chain[:] + [num]

    chains = []
    for i in range(3):
        next_index = current + i + 1
        if next_index < len(to_check):
            next_num = to_check[next_index]
            if next_num - num <= 3:
                build = build_chain(to_check, next_index, new_chain)
                if len(build) == 0:
                    chains += [[num]]
                else:
                    chains += [[num] + b for b in build]
            else:
                chains += [[next_num]]1
    return chains

def part2():
    breaks = []
    for i in range(len(raw[:-1])):
        if raw[i+1] - raw[i] == 3:
            breaks += [i+1]
    breaks = [0] + breaks + [len(raw)]
    steps = zip(breaks, breaks[1:])

    result = 1
    for (start, end) in steps:
        data = raw[start:end]
        chains = build_chain(data)
        chain_len = len(chains)
        if chain_len > 0:
            result *= chain_len
    print(result)

# part1()
part2()