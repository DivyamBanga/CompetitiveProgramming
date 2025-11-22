class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        operations=0
        for i in range(len(nums)):
            if nums[i]%3==0:
                pass
            elif nums[i]%3==1:
                nums[i]-=1
                operations+=1
            elif nums[i]%3==2:
                nums[i]+=1
                operations+=1
        return operations
            
        