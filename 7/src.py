import re

reg = r"([a-z]+ [a-z]+) bags contain (?:no other bags|((?:\d (?:(?:[a-z]+ [a-z]+) bags?(?:, )?))+))."
reg_bag = r"(\d) ([a-z]+ [a-z]+) bags?(?:, )?"

bag_graph = {}
def make_node(name, children): {'name': node}

rules = open('input.txt').read().splitlines()
for rule in rules:
    [bag_name, children] = re.match(reg, rule).groups()
    bag_graph.setdefault(bag_name, {})

    if children:
        for [count, child_name] in re.findall(reg_bag, children):
            bag_graph[bag_name][child_name] = int(count)

def part1():
    def recurse(tree, entry):
        if 'shiny gold' in tree: return entry
        if type(tree) == int: return None
        for i in tree:
            val = recurse(bag_graph[i], entry)
            if val: return entry

    a = list(filter(lambda x: x, [recurse(bag_graph[i], i) for i in bag_graph]))
    print(len(a))

def part2():
    def recurse(tree):
        if tree == {}:
            return 0
        total = 0
        for child in tree:
            total += recurse(bag_graph[child]) * tree[child] + tree[child] 
        return total

    print(recurse(bag_graph['shiny gold']))

# part1()
part2()