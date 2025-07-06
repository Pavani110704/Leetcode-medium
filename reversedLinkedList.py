# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next  # store next node
            current.next = prev       # reverse link
            prev = current            # move prev forward
            current = next_node       # move current forward

        return prev  # new head of the reversed list
