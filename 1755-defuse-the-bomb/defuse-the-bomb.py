class Solution(object):
    def decrypt(self, code, k):
        """
        :type code: List[int]
        :type k: int
        :rtype: List[int]
        """

        length=len(code)
        ans=[0]*length
        if k==0:
            for i in range(len(code)):
                code[i]=0
            return code
        if k>0:
            for i in range(len(code)):
                total=0
                for j in range(k):
                    total+=code[(i+j+1)%length]
                    print(total)
                ans[i]=total
            return ans
        if k<0:
            for i in range(len(code)):
                total=0
                for j in range(abs(k)):
                    total+=code[(i-j-1)%length]
                    print(total)
                ans[i]=total
            return ans

        