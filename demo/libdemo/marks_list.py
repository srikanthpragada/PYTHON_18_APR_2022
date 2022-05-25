f = open("marks.txt", "rt")

for line in f.readlines():
    # split line after removing whitespace using strip()
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue    # ignore line as it has not enough data

    name = parts[0]
    # Second part onwards marks. But ignore parts that are not numbers
    marks = list(filter(str.isdigit, parts[1:]))
    # Convert marks in the form of str to int using map()
    total = sum(map(int, marks))
    print(f"{name:20} {total:4}  {total/len(marks):5.2f}")

f.close()
