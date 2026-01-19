import random
random_number1 = ""
for _ in range(3):
    random_number1 += str(random.randint(0, 9))
random_number2 = ""
for _ in range(4):
    random_number2 += str(random.randint(1, 6))
print("3-digit code:", random_number1)
print("4-digit code:", random_number2)