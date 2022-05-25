f = open("names.txt", "rt")

for line in f.readlines():
    print(line, end='')

f.readline()
f.close()
