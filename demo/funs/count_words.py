
def count_words(s):
    count = 0
    for c in s:
        if c == ' ':
            count += 1

    return count + 1


print(count_words('This is fine'), count_words("Hello there"))