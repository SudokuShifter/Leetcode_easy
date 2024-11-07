class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        vowels = {'a', 'e', 'i', 'o', 'u'}
        new_str = list(s)
        vowels_in_str = [i for i in new_str if i.lower() in vowels]
        vowels_in_str.reverse()
        ind = 0
        for i, chr in enumerate(new_str):
            if chr.lower() in vowels:
                new_str[i] = vowels_in_str[ind]
                ind += 1
        return ''.join(new_str)