import itertools
from typing import Iterator

with open('input.txt') as f:
    readings = f.readlines()
readings = [int(line.rstrip('\n')) for line in readings]


def num_increases(num: Iterator[int]):
    return sum((b > a for a, b in itertools.pairwise(num)))


def take_n(num, n):
    return ((num[i-(n-1):i+1]) for i in range(n-1, len(num)))


def main():
    print('part1:', num_increases(readings))
    print('part2:', num_increases(map(sum, take_n(readings, 3))))


if __name__ == '__main__':
    main()
