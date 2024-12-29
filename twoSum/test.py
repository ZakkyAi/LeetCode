class Solution(object):
    def twoSum(self, nums, target):
        simpan_nomor = {}  # Dictionary to store the number and its index
        
        for index, num in enumerate(nums):  # Correct usage of enumerate
            hasil = target - num  # Correct subtraction

            if hasil in simpan_nomor:  # Check if the result exists in the dictionary
                return [simpan_nomor[hasil], index]  # Return indices of the two numbers
            
            simpan_nomor[num] = index  # Store the current number and its index in the dictionary

# Test case
solution = Solution()
result = solution.twoSum([2, 7, 11, 15], 13)
print(result)  # Expected output: [0, 1]