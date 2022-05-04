def compare(s1, s2):
    for idx, c1 in enumerate(s1):
        if c1 != s2[idx]:
            return idx

    return None


print(compare("Abc", "Abc"))
print(compare("Axc", "Abc"))
