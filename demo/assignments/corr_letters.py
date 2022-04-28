s1 = "AbcDefpp"
s2 = "AcbDpf"

sl = min(len(s1), len(s2))

for i in range(sl):
    if s1[i] == s2[i]:
        print(s1[i])



