import itertools
from typing import Iterator

with open('input.txt') as f:
    readings = f.readlines()
readings = [int(line.rstrip('\n')) for line in readings]

def num_increases(num: Iterator[int]):
    return sum((b > a for a, b in itertools.pairwise(num)))

def take_three(it: Iterator[int]):
    return ((it[i-2:i+1]) for i in range(2, len(it)))

def sum_three(nums: Iterator[int]):
    return (sum(i) for i in take_three(nums))


def main():
    print('part1:', num_increases(readings))
    print('part2:', num_increases(sum_three(readings)))

if __name__ == '__main__':
    main()