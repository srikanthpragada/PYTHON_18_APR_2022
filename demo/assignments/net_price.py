# Show net price after 10% discount

data = input("Enter price : ")
price = float(data)     # Convert str to int
discount = price * 10 / 100
netprice = price - discount

print(f"Price      {price:8.2f}")
print(f"-Discount  {discount:8.2f}")
print(f"Net price  {netprice:8.2f}")

