num = 38

while num >= 10:
    cur = num
    new_num = 0

    while cur:
        cur, d = divmod(cur, 10)
        new_num += d

    num = new_num


a = [1, 2, 3]
b = [1, 2, 3]

print(id(a), id(b))