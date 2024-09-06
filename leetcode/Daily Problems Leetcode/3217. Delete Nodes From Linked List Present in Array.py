# You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

# Input: nums = [5,4,2], head = [1,2,3,4,5]

# Output: [1,3]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next:
            if prev.next.val in nums:
                prev.next = prev.next.next
            else:
                prev = prev.next
        
        return dummy.next
