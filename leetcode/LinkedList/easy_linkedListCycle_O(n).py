# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # if( head.next == None): return False
        cur = head
        listNodeSet = set()
        while(cur != None):
            if(cur not in listNodeSet):
                listNodeSet.add(cur)
                cur = cur.next
            else:
                return True
        return False