with open('input.txt') as f:
        readings = f.readlines()
readings = [int(line.rstrip('\n')) for line in readings]
        
