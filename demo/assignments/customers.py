
data = ["Scott,989898984343", "Tom,38383833333",
        "Joe,39393933443", "Tom,28388223232", "Brian,3939423232"]

customers = {}
for entry in data:
    name, mobile = entry.split(",")
    customers[name] = mobile

for name, mobile in sorted(customers.items()):
    print(f"{name:15} {mobile}")
