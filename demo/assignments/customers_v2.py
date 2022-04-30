data = ["Scott,989898984343", "Tom,38383833333", "Brian,39394232432",
        "Joe,39393933443", "Tom,28388223232", "Tom,28388223232",
        "Brian,3939423232"]

customers = {}
for entry in data:
    name, mobile = entry.split(",")
    lst = customers.get(name, [])
    lst.append(mobile)
    customers[name] = lst

for name, mobiles in sorted(customers.items()):
    print(f"{name:15} {','.join(mobiles)}")
