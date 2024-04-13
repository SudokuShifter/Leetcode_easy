x = 101

left = 1
right = x


while right - left > 1:
    middle = (left + right) // 2
    if middle * middle > x:
        right = middle
    else:
        left = middle

print(left)
