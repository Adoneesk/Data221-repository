from random import random

values = [random() for i in range(20)]
randomValue = random()

values.sort()
comparison_index = []
first_matching_index = None

for i in values:
    if i >= randomValue:
        comparison_index.append(i)
for i in values:
    if i == randomValue:
        first_matching_index = i
        break #
print(values)
print(randomValue)
if first_matching_index != None:
    print(first_matching_index)

