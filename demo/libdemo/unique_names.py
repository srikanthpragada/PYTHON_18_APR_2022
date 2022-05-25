with open("names.txt", "rt") as f:
    lines = map(lambda l: l.strip(), f.readlines())
    sortednames = sorted(set(filter(lambda l: len(l) > 0, lines)))
    for name in sortednames:
        print(name)

