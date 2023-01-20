# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        num = ''
        current = head
        while current:
            num = num + str(current.val)
            if current.next:
                current = current.next
            else:
                break
        return int(num,2)
