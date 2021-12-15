with open('input.txt') as f:
    readings = f.readlines()
readings = [int(line.rstrip('\n')) for line in readings]

def counting(r):
    count = 0
    for i in range(1,len(r)):
        if r[i-1] < r[i]:
            count += 1
    return count

count = counting(readings)
print(count)
# %%
