# Q4. Create a program that prints the multiplication table of a given number.

n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} * {i} = {n*i}")