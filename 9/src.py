raw = [int(i) for i in open('input.txt').read().splitlines()]

def find_weakness(nums, size):
    for i, num1 in enumerate(nums[size:]):
        r = i+size
        found = False
        for j, num2 in enumerate(nums[r-size:r]):
            exists = abs(num1 - num2) in nums[r-size:r]
            if exists:
                found = True
                break
        if not found:
            return num1

def probe_weakness(nums, fault):
    for x in range(len(nums)):
        for y in range(len(nums)):
            if sum(nums[x:y]) == fault:
                return(min(nums[x:y]) + max(nums[x:y]))


def part1(): print(find_weakness(raw, 25))
def part2(): print(probe_weakness(raw, find_weakness(raw, 25)))

# part1()
part2()