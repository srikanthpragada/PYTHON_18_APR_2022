# Keyword-only args
def wish(*, name="Guest", msg='Hi'):
    print(msg, name)


# wish("Hello", "Scott")
wish(name="Mark", msg="Hello")
