class Solution(object):
    def distributeCandies(self, candyType):
        max_candies = len(candyType) 

        unique_types = len(set(candyType))
        return min(max_candies, unique_types)