# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        finalLL = ListNode()
        stack1 = []
        stack2 = []
        finalStack = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        while len(stack1) > 0 and len(stack2) > 0:
            x = stack1.pop()
            y = stack2.pop()
            print(x,y,carry,stack1)
            s = x+y+carry
            res = s%10
            carry = s//10
            finalStack.append(res)
        while len(stack1) > 0:
            x = stack1.pop()
            finalStack.append(x+carry)
            carry = 0
        while len(stack2) > 0:
            x = stack2.pop()
            finalStack.append(x+carry)
            carry = 0
        if carry>0:
            finalStack.append(carry)
        curNode = None
        prevNode = None
        for num in finalStack:
            if curNode:
                prevNode = curNode
            curNode = ListNode(num)
            curNode.next = prevNode
        print(finalStack)
        return curNode
        