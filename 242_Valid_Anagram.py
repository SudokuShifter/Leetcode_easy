s = "anagram"
t = "nagaraZXm"

if len(s) != len(t):
    print(False)

for i in set(s):
    if s.count(i) != t.count(i):
        print(False)

print(True)