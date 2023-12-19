import numpy as np

list = [98, 141, 135, 119]

vals = []

for n in list:
    vals.append((n - np.average(list))**2)

total = 0

for n in vals:
    total += n

print(total / (len(list)-1))
print(np.sqrt((total / (len(list)-1))))
