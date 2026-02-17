cost_price = float(input("Enter the cost price of the book: "))
discount_percent = float(input("Enter the discount percentage: "))

# formula for calculating discount amount
discount_amount = (cost_price * discount_percent) / 100

# formula for calculating selling price
selling_price = cost_price - discount_amount

print("Discount Amount =", discount_amount)
print("Selling Price =", selling_price)
