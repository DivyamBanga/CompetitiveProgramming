class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final=[]
        for j in range(2):
            for i in nums:
                final.append(i)
        return final
        