import re

vd = {'byr': lambda x: int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: int(x) >= 2010 and int(x) <= 2020,
    'eyr': lambda x: int(x) >= 2020 and int(x) <= 2030,
    'hgt': lambda x: (x[-2:] == 'cm' and int(x[:-2]) >= 150 and int(x[:-2]) <= 193) or (x[-2:] == 'in' and int(x[:-2]) >= 59 and int(x[:-2]) <= 76),
    'hcl': lambda x: bool(re.search(r'#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', x)),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: len(x) == 9 and x.isnumeric()}

def part1(): print([all([x in [cred[:3] for cred in row.replace('\n', ' ').split(' ')] for x in vd.keys()]) for row in open('input.txt').read().split('\n\n')].count(True))
def part2(): print([all([x in [cred[:3] if vd.get(cred[:3], lambda x: False)(cred[4:]) else None for cred in row.replace('\n', ' ').split(' ')] for x in vd.keys()]) for row in open('input.txt').read().split('\n\n')].count(True))

# part1()
part2()