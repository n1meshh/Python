#separate negative and positive number from list

l = [1,2,-9,8,-3,45,-19]
print("Positive numbers are:")
for i in range(len(l)):
    if l[i]>=0:
        print(l[i])
print("Negative numbers are:")
for i in range(len(l)):
    if l[i] < 0:
        print(l[i])