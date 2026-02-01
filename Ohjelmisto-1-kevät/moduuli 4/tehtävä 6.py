import random
N = int(input())
count_inside_circle = 0
i = 0
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        count_inside_circle += 1
    i += 1
pi_approx = 4 * count_inside_circle / N
print("Approximation of pi:", pi_approx)