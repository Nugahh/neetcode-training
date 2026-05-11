# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        curr = l1
        while curr:
            num1 = str(curr.val) + num1
            curr = curr.next
        curr = l2

        while curr:
            num2 = str(curr.val) + num2
            curr = curr.next
        
        total = int(num1) + int(num2)
        listNum = []
        for n in str(total):
            listNum.append(int(n))
        dummy = ListNode(0)
        curr = dummy
        for val in listNum[::-1]:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next