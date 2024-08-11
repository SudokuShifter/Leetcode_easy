class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        l = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y']
        s = ''
        while columnNumber > 0:

            s += l[columnNumber % 26]

            if columnNumber % 26 == 0:
                columnNumber = (columnNumber // 26) - 1
            else:
                columnNumber = columnNumber // 26

        return s[::-1]