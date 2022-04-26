s = "Abc123Pqr45"

count = 0
for c in s:
    if c.isdigit():
        count += 1

print("No. of digits = ", count)
