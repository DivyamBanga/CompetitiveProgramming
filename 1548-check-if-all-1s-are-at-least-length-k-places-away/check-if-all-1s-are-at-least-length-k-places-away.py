class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count=0
        seen=False
        for i in range(len(nums)):
            if i==0:
                if nums[i]!=1:
                    count+=1
                else:
                    seen=True
            else:
                if nums[i]==1:
                    if count<k and seen==True:
                        return False
                    else:
                        seen=True
                        count=0
                else:
                    count+=1
                print(count)
        return True