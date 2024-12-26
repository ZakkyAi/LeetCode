class Solution(object):
    def reverseWords(self, satu):
        titit = satu.split()  # Split the string into words
        besar = titit[::-1]   # Reverse the list of words
        hasil = " ".join(besar)  # Join the reversed words into a single string
        return hasil

solution = Solution()
result = solution.reverseWords("the sky is blue")
print(result)  # Output: "blue is sky the"
