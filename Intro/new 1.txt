# Total price
price = float(input("Total computer cost:"))

# Price after down payment
remaining_price = (price * 0.9)

# Monthly payment (5 percent of remaining price)
monthly_payment = remaining_price * 0.05

# Interest owed for this month
interest_owed = remaining_price * (.12/12.0)

# Principal for this month
principal = monthly_payment - interest_owed

# Month 
month = 0

# Print stuff
print("%0d Months%20.2f%20.3f%20.2f%13.2f%23.2f" %(month, price, interest_owed, principal, monthly_payment, remaining_price))

while remaining_price > 0:
    month += 1
    remaining_price -= principal
    interest_owed = remaining_price * (.12/12.0)
    principal = monthly_payment - interest_owed

    print("%0d Months%20.2f%20.3f%20.2f%13.2f%23.2f" %(month, price, interest_owed, principal, monthly_payment, remaining_price))