def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    list_s = list(s)
    i = 0
    j = len(list_s) - 1
    while i < j:
        if list_s[i] in vowels and list_s[j] in vowels:
            list_s[i], list_s[j] = list_s[j], list_s[i]
            i += 1
            j -= 1
        elif list_s[i] not in vowels:
            i += 1
        else:
            j -= 1
    return ''.join(list_s)


print(reverseVowels("Marge, let's \"went.\" I await news telegram."))