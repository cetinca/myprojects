class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_ = len(s)
        char = True
        i = -1
        word = ""
        while abs(i) <= len_:
            char = s[i]
            if char == " " and word == "":
                i -= 1
            elif char == " ":
                break
            else:
                i -= 1
                word += char

        # new_word = ""
        # for i in range(len(word)-1, -1, -1):
        #     new_word += word[i]

        return len(word)