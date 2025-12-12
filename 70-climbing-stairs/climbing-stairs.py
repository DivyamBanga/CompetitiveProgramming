class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways=1
        count=1
        for i in range(0,n/2):
            ways+=(factorial(n-count)/((factorial(count))*factorial(n-2*count)))
            count+=1
        return ways