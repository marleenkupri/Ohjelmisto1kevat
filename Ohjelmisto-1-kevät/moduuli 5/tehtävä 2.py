number = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    number.append(float(user_input))

number.sort(reverse=True)

print("The greatest numbers in descending order:")
for n in number[:5]:
    print(n)