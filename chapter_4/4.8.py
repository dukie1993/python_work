numbers = []
for value in range(1, 11):
    sq = value ** 3
    numbers.append(sq)
for value in numbers:
    print(value)
print('The first three items in the list are:', numbers[:3])
print('Three items from the middle of the list are:', numbers[4:7])
print('The last three items in the list are:', numbers[-3:])