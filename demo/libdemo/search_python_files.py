import os


def file_has_string(filename, text):
    try:
        with open(filename, "rt") as f:
            contents = f.read()
            return text in contents
    except:
        return False


stdir = r"d:\classroom\apr18\demo"
ss = "print"

allfiles = os.walk(stdir)
count = 0
for dirname, folders, files in allfiles:
    for f in files:
        if f.endswith(".py"):
            filename = dirname + "\\" + f
            if file_has_string(filename, ss):
                print(filename)
