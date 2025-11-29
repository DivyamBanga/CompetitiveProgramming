class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        for num in nums:
            if nums.count(num)>1 and num not in result:
                result.append(num)
        return result


        