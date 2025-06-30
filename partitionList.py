class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        before_head = ListNode(0)  # Dummy head for < x
        after_head = ListNode(0)   # Dummy head for >= x
        before = before_head
        after = after_head

        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next
            current = current.next

        # End the 'after' list and link 'before' to 'after'
        after.next = None
        before.next = after_head.next

        return before_head.next
