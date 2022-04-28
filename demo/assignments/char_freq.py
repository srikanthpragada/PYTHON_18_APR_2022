
st = "How do you do"

chars = []
for c in st:
    if c not in chars:
       print(f"{c} occurs for {st.count(c)} time(s)")
       chars.append(c)

