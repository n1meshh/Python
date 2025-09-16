# Accept a number and print its reverse and also check the palindrome

n = int(input("Tell your number:-"))

rev = 0
a = n
while n>0:
    rev = rev * 10 + n%10
    n = n//10

if rev == a :
    print("Palindrome")
else:
    print("Not palindrome")