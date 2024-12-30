class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        return x == x[::-1]

Solution = Solution()
print(Solution.isPalindrome(11))