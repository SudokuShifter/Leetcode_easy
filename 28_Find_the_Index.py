haystack = "hello"
needle = "ll"
hm = []

for i in range(len(haystack)):
    if haystack[i:len(needle)+i] == needle:
        hm.append(i)

print(hm)

if hm:
    print(hm[0])
else:
    print('0')