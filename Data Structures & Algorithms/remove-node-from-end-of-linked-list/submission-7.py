# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        index = count - n
        if index == 0:
            return head.next
        
        curr = head
        for i in range(count):
            if i + 1 == index:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head