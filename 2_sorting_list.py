# Sort list into two lists

numbers = [1, -5, 2, -4, 0, 6, -10, 3]
pos = []
neg = []

print("List of numbers")
for number in numbers:
    print (number)
print()

for number in numbers:
    if number > 0:
        pos.append(number)
    else:
        neg.append(number)

print("Positives: ", pos)
print("Negatives ", neg)

print()

# Alternative solution

print("List comprehension in single lines of code:")
pos = [i for i in numbers if i > 0]
neg = [i for i in numbers if i < 0]
print("Positives: ", pos)
print("Negatives ", neg)