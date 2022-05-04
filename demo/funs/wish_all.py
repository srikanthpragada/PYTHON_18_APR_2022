def wish(*names, msg="Hi"):
    print(type(names))
    for n in names:
        print(msg, n)


wish("Jack", "Joe", "Bob", msg="Hello")
wish("Scott", msg = "Good Morning",)
