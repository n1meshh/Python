#find the greatest element and find its index too

l = [23,53,4,6578,3,4,2,12,13,243]

largest = l[0]
index = 0

for i in range (len(l)):
    if l[i] > largest:
        largest = l[i]
        index = i
    
print(f"The largest number is {largest} and it is in index {index }")