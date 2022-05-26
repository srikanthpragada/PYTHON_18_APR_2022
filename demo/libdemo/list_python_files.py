import os

stdir = r"d:\classroom\apr18\demo"
allfiles = os.walk(stdir)
count = 0
for dirname, folders, files in allfiles:
    for f in files:
        if f.endswith(".py"):
            print( dirname + "\\" + f)
            count += 1

print(f"Count = {count}")



