import random
code3 = ""
for i in range(3):
    code3 += str(random.randint(0, 9))
code4 = ""
for i in range(4):
    code4 += str(random.randint(1, 6))
print(code3)
print(code4)