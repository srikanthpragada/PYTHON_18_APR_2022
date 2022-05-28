import re

customers = {}

f = open("customers.txt", "rt")
for line in f.readlines():
    # look for name
    m = re.search('[a-zA-Z ]+', line)
    if m is None: # name not found
        continue

    name = m.group().strip()

    # Look for mobile
    m = re.search(r'\d+', line)
    if m is None: # mobile not found
        continue

    mobile = m.group()

    customers[name] = mobile

f.close()

for name, mobile in sorted(customers.items()):
    print(f"{name:20} {mobile}")
