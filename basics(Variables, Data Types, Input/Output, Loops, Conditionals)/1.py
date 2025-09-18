#program to swap two variables

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))

print(f"The two numbers before swapping are {n1} and {n2}")

temp = n1
n1 = n2
n2 = temp

print(f"The two numbers after swapping are {n1} and {n2}")

