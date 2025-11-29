class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        total=0

        totals=[]

        while n!=1:
            for i in str(n):
                total+=int(i)**2
            n=total
            totals.append(n)
            total=0

            if len(totals)>7:
                return False
            
        return True
