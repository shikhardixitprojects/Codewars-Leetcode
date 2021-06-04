# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while(head != None):
            if(head.next != None and head.next.val == head.val):
                if(head.next.next != None):
                    head.next = head.next.next
                else:
                    head.next = None
            else:
                head = head.next
        return cur
            
        