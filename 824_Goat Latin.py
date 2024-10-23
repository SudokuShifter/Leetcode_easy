class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        new_sentence = sentence.split()
        result = []
        for i in range(len(new_sentence)):
            first_letter = new_sentence[i][0]
            if first_letter.lower() in vowels:
                result.append((new_sentence[i] + 'ma') + 'a' * (i + 1))  
            else:
                result.append((new_sentence[i][1:] + first_letter + 'ma') + 'a' * (i + 1))
        return ' '.join(result)