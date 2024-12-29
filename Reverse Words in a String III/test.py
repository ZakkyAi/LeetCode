class Solution(object):
    def reverseWords(self, input_arg):
        hasil_input_arg = input_arg.split()  # Split the string into words
        besar = hasil_input_arg[::-1]   # Reverse the list of words
        hasil = " ".join(besar)  # Join the reversed words into a single string
        return hasil

solution = Solution()
result = solution.reverseWords("the sky is blue")
print(result)  # Output: "blue is sky the"
