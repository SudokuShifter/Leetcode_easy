s = "anagram"
t = "nagaram"

if len(s) != len(t):
    print(False)

dist = len(s)
for i in set(s):
    if s.count(i) != t.count(i):
        print(False)

print(True)