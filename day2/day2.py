
from math import radians


with open('input.txt') as f:
    readings = f.readlines()
readings = [line.rstrip('\n') for line in readings]


def part1(r):
    location = complex(0,0)
    for i in r:
        d, n = i.split(' ')
        n = int(n)
        match d:
            case 'forward':
                location += complex(n,0)
            case 'down':
                location += complex(0,n)
            case 'up':
                location += complex(0,-n)
    return int(location.real * location.imag)

def part2(r):
    location = complex(0,0)
    aim = 0
    for i in r:
        d, n = i.split(' ')
        n = int(n)
        match d:
            case 'forward':
                location += complex(n,aim * n)
            case 'down':
                aim += n
            case 'up':
                aim -= n
    return int(location.real * location.imag)

print('part1', part1(readings))
print('part2', part2(readings))