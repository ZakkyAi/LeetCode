class Solution(object):
    def numJewelsInStones(self, jewels, stones):

        hasil_jewels = list(jewels)
        hasil_stones = list(stones)
        print(hasil_jewels)
        print(hasil_stones)
        print(jewels)
        print(stones)


        total = 0
        for stone in hasil_stones:
            if stone in hasil_jewels:
                total += 1
            else:
                continue
        return total


solution = Solution()
print(solution.numJewelsInStones("aA", "aAAbbbb"))