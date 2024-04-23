s = ["h", "e", "l", "l", "o"]

dist = len(s)
i = 0
while i != dist//2:
    s[i], s[dist - i - 1] = s[dist - i - 1], s[i]
    i += 1

print(s)