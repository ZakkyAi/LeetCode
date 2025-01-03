class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(n) if nums[i] > 0]

# Create an instance of the Solution class
solution = Solution()

