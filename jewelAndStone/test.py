class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        hasil_jewels = jewels.split()
        hasil_stones = stones.split()
        split_jewels = hasil_jewels
        split_stones = hasil_stones


solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))