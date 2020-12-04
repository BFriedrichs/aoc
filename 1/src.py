import os

nums = []

with open('input.txt') as fh:
    text = fh.read()

    nums = [int(i) for i in ''.join(list(text)).split('\n')]

for num1 in nums:
    for num2 in nums:
        for num3 in nums:
            if num1 + num2 + num3 == 2020:
                print(num1 * num2 * num3)
                exit()