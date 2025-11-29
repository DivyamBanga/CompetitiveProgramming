class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        while True:
            if sum(nums)%k==0:
                return count
            else:
                nums[0]-=1
                count+=1

        