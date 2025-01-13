class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  
            curr.next = prev      
            prev = curr            
            curr = next_node       
        return prev
         


Solution = Solution()
print(Solution.reverseList([1, 2, 3, 4, 5]))
print(Solution.reverseList([1, 2]))
print(Solution.reverseList([1]))

# Create a ListNode class
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Convert the list to a linked list
def list_to_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for num in lst:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Convert the linked list to a list
def linked_list_to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

# Test the function
Solution = Solution()
print(linked_list_to_list(Solution.reverseList(list_to_linked_list([1, 2, 3, 4, 5]))))
print(linked_list_to_list(Solution.reverseList(list_to_linked_list([1, 2]))))
print(linked_list_to_list(Solution.reverseList(list_to_linked_list([1]))))

