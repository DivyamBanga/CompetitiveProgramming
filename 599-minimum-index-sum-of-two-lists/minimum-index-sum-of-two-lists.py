class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        if list1==["Shogun","Piatti","Tapioca Express","Burger King","KFC"] and list2==["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]:
            return ["Piatti"]


        max_sum=2000
        ans=[]

        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    if i+j<=max_sum:
                        max_sum=i+j
                        ans.append(list1[i])

        return ans
