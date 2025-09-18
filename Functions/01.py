# ATM Cash Withdrawal
# Write a function atm_withdraw(balance, amount) that checks if the withdrawal amount is less than or equal to the balance.

# If yes, subtract and return the new balance.

# If not, return "Insufficient funds".

def atm_withdraw(amount, balance=1000):
    if amount < balance:
        totalAmount = balance - amount
        print(f"Amount withdraw succesfully{amount}")
        print(f"Remaining Amount is {totalAmount}")
    else :
        print("Insufficent funds ")

amount = int(input("Enter the amount you want to withdraw: "))

atm_withdraw(amount)

