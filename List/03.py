#calculate mean from list: 1,2,3,4 = 1+2+3+4 / 4  = 2.5

l = [1,2,3,4,5]
sum = 0
for i in range(len(l)):
    sum = sum + l[i]

mean = sum / len(l)

print("The mean is ", mean)