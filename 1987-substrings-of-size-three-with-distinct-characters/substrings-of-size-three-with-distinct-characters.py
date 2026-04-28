class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def check(word):
            seen_letters = []
            for letter in word:
                if letter in seen_letters:
                    return False
                seen_letters.append(letter)
            return True

        length = len(s)
        count=0

        for i in range(length-2):
            sub=""
            for j in range(3):
                sub+=s[(i+j)]
            print(sub)
            if check(sub):
                count+=1
        return count



        