# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        if not l1 and not l2:
            return l1
        elif not l1:
            return l2
        elif not l2:
            return l1
        newl = ListNode(-1)
        head = newl
        while (l1 != None and l2 != None):
            if l1.val > l2.val:
                t = l2.next
                newl.next = l2
                newl = l2
                l2 = t
            elif l1.val <= l2.val:
                t = l1.next
                newl.next = l1
                newl = l1
                l1 = t
            if not l1 and l2:
                newl.next = l2
                break
            elif not l2 and l1:
                newl.next = l1
                break
        return head.next
                
        