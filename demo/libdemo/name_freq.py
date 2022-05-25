f = open("names.txt", "rt")

names = {}
for name in f.readlines():
    name = name.strip()
    if len(name) == 0:  # ignore as empty line
        continue

    if name in names:  # found in dict so increment count
        names[name] = names[name] + 1
    else:  # not found so add new key with 1 as value
        names[name] = 1

f.close()

for name, count in sorted(names.items()):
    print(f"{name:15} {count:2}")
