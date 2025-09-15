# check palindrome or not
a = input("Enter the word to check palidrome:")

b =''
for i in range(len(a)-1 , -1 , -1):
    b = b+a[i]

if b == a:
    print("palindrome")
else:
    print("not palindrome")