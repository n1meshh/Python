#print sum of all even and odd number in range separeatly:

n = int(input("Enter the number:-"))

even = 0
odd = 0

for i in range(1 , n+1):
    if i%2 == 0:
        even = even + i
    else:
        odd = odd + i
    
print(f"The sum of even and odd is {even} and {odd}")