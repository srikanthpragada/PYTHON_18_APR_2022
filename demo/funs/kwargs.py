def show(**kwargs):
    print(type(kwargs))


def details(*args, **kwargs):
    pass


show(name="Python", version="3.10")
show(x=10, y=20)

details(10, 20, x=10, y=20)
