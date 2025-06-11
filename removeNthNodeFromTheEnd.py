class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy
        
        # Move fast ahead by n + 1 steps to create a gap of n
        for _ in range(n + 1):
            fast = fast.next
        
        # Move both fast and slow until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # Remove the nth node from end
        slow.next = slow.next.next
        
        return dummy.next