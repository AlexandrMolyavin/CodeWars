https://www.codewars.com/kata/5540b8b79bb322607b000021
class SpreadSheetHelper(object):

    def convert_to_display(self, internal):
        n = internal[0] + 1
        string = ""
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            string = chr(65 + remainder) + string
        return string + str(internal[1] + 1)

    def convert_to_internal(self, display):
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        s1 = ''
        s2 = ''
        for i in display:
            if i.isalpha():
                s1 += i
            else:
                s2 += i
        expn = 0
        col_num = 0
        for char in reversed(s1):
            col_num += (ord(char) - ord('A') + 1) * (26 ** expn)
            expn += 1

        return (col_num - 1, int(s2) - 1)


SpreadSheetHelper = SpreadSheetHelper()
