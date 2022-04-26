# Show net price after 10% discount

data = input("Enter price : ")
price = int(data)     # Convert str to int
discount = price * 10 // 100
netprice = price - discount

print("Net price = ", netprice)
