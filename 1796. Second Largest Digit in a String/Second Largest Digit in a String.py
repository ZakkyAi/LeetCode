class Solution(object):
    def secondHighest(self, s):
        numbers = [int(item) for item in s if item.isdigit()]
        unique_numbers = list(set(numbers))
        if len(unique_numbers) < 2:
            return -1
        return sorted(unique_numbers, reverse=True)[1]
