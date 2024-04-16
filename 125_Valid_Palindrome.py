import string

s = '"A man, a plan, a canal: Panama"'

if s == ' ':
    print(True) 

s = list(filter(lambda i: i not in string.punctuation, s))
s = ''.join(s).replace(' ', '').lower()
print(s == s[::-1]) 