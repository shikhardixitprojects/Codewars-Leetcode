# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeSet = set()
        while(head != None):
            if(head not in nodeSet):
                nodeSet.add(head)
            else:
                return head
            head = head.next
        return None