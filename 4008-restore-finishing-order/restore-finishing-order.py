class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        final=[]
        for i in order:
            if i in friends:
                final.append(i)
        return final
        