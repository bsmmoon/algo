# Approach 1.
# check how many nodes are there in each linked list O(N)
# start the longer one with the differences step earlier so that longer and shorter would reach the intersection at the same time O(N)

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        alength = 0
        node = headA
        while node:
            node = node.next
            alength += 1
            
        blength = 0
        node = headB
        while node:
            node = node.next
            blength += 1
            
        if alength > blength:
            diff = alength - blength
            while diff > 0:
                headA = headA.next
                diff -= 1
        else:
            diff = blength - alength
            while diff > 0:
                headB = headB.next
                diff -= 1
        
        while headA != headB: headA, headB = headA.next, headB.next
        
        return headA
