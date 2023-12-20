#!/usr/bin/env python
import re


def get_max(line: str, colour: str):
    match = re.findall(rf'(?P<number>\d+) {colour}', line)
    return max([int(e) for e in match])


if __name__ == '__main__':
    sum = 0
    with open('day2data.txt') as file:
        content = file.read()

    for line in content.split('\n'):
        sum += get_max(line, 'red') * get_max(line, 'green') * get_max(line, 'blue')

    print(sum)
