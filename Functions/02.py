# Movie Ticket Pricing

# Kids below 12: Rs. 100

# Teen (13–17): Rs. 150

# Adult (18+): Rs. 250
# Write a function ticket_price(age) that returns the price.
# Then, write a loop that asks for ages of 5 people and prints their total cost.
def ticket_price(age):
    if age < 12:
        price = 100
        
