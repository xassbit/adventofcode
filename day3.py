#!/usr/bin/env python
from typing import Optional


def valid_numbers(line: str, previous_line: Optional[str], next_line: Optional[str]):
    result = []
    i = 0
    number = ''
    while i < len(line):
        if line[i] not in '1234567890':
            i += 1
            continue

        number = f'{number}{line[i]}'

        if i + 1 == len(line) or line[i + 1] not in '1234567890':
            characters = ''
            if previous_line:
                characters += previous_line[max(i - len(number), 0):min(i + 2, len(line))]
            if next_line:
                characters += next_line[max(i - len(number), 0):min(i + 2, len(line))]
            if i - len(number) > 0:
                characters += line[i - len(number)]
            if i + 1 < len(line):
                characters += line[i + 1]

            if len(set(characters).difference(set('1234567890.'))) != 0:
                result.append(int(number))

            number = ''

        i += 1
    return result


if __name__ == '__main__':
    total = 0
    with open('day3data.txt') as file:
        content = file.read().split('\n')

    i = 0
    while i < len(content):
        line = content[i]
        previous_line = content[i - 1] if i > 0 else None
        next_line = content[i + 1] if i + 1 < len(content) else None
        numbers = valid_numbers(line, previous_line, next_line)
        total += sum(numbers)
        i += 1

    print(total)
