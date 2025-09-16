#separte each digits of number and print it on separate line:

n = int(input("Tell your number:-"))

while n > 0:
    print(n%10)
    n = n // 10