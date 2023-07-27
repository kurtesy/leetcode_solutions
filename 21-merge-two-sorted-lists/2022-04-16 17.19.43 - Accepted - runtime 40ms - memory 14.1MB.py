# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = list1
        ptr2 = list2
        if not ptr1:
            return ptr2
        if not ptr2:
            return ptr1
        res = ListNode()
        head = res
        while ptr1 and ptr2:
            print(ptr1.val, ptr2.val)
            if ptr1.val == ptr2.val:
                newNode = ListNode(ptr2.val)
                res.next = newNode
                newNode = ListNode(ptr1.val)
                res = res.next
                res.next = newNode
                ptr1 = ptr1.next
                ptr2 = ptr2.next
            elif ptr1.val < ptr2.val:
                newNode = ListNode(ptr1.val)
                res.next = newNode
                ptr1 = ptr1.next
            elif ptr1.val > ptr2.val:
                newNode = ListNode(ptr2.val)
                res.next = newNode
                ptr2 = ptr2.next
            res = res.next
        if ptr1:
            res.next = ptr1
        if ptr2:
            res.next = ptr2
        print(ptr1, ptr2)
        return head.next
        
        