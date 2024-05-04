def isHappy(n: int) -> bool:
    a = set()
    while n != 1 and n not in a:
        a.add(n)
        n = sum(int(x)**2 for x in str(n))
    return n == 1