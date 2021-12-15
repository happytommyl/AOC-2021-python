
with open('input.txt') as f:
    readings = f.readlines()
readings = [int(line.rstrip('\n')) for line in readings]

def group(r):
    grouped_readings = [readings[i] + readings[i+1] + readings[i+2] for i, _ in enumerate(r[:-2])]
    return grouped_readings

grouped_readings = group(readings)

def counting(r):
    count = 0
    for i in range(1,len(r)):
        if r[i-1] < r[i]:
            count += 1
    return count

count = counting(grouped_readings)
print(count)