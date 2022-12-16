# List comperehension

print('Randomize the numbers 1 - 26')
import random
numbers = [i for i in range(1,26)]
random.shuffle(numbers)
print(numbers)

print('Random list of numbers')
shuffled_horses = [9, 7, 18, 20, 3, 8, 14, 22, 10, 19, 1, 4, 11, 16, 17, 21, 23, 24, 12, 15, 13, 25, 6, 2, 5]
print(shuffled_horses)
print()

print('Put the random list in groups of 5')
horses= [[],[],[],[],[]]

for i in range(5):
    for j in range (5):
        horses[j].append(shuffled_horses.pop())

print(horses)
print()

print('Sort the horses in each race')
for race in horses:
    race.sort()
    print(race)
print()

print('Sort the races descending by highest number')
def last (x):
    return x[-1]

horses_sorted = sorted(horses, key=last, reverse=True)

for race in horses_sorted:
    print(race)

print()
print(horses_sorted[0] [2:])
print(horses_sorted[1] [3:])
print(horses_sorted[2] [-1])
