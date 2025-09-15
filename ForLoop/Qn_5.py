#sum upto n number

n = int(input("Enter the number:-"))

total = 0
for i in range(1, n+1):
    total = total + i
print("Sum up to", n, ":", total)