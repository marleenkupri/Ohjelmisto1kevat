import random
amount = int(input("How many dice to roll: "))
total = 0
for i in range(amount):
    total += random.randint(1, 6)
print(f"Sum of the dice:", total)