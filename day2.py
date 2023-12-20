#!/usr/bin/env python
import re


def get_game_id(line: str):
    match = re.match(r'^Game (?P<number>\d+)', line)
    return int(match.group('number'))


def exceeds_limit(line: str, colour: str, limit: int):
    match = re.findall(rf'(?P<number>\d+) {colour}', line)
    return any([int(e) > limit for e in match])


if __name__ == '__main__':
    sum = 0
    with open('day2data.txt') as file:
        content = file.read()

    for line in content.split('\n'):
        if (
                exceeds_limit(line, 'red', 12) or
                exceeds_limit(line, 'green', 13) or
                exceeds_limit(line, 'blue', 14)
        ):
            pass
        else:
            sum += get_game_id(line)

    print(sum)
