class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head

        # Compute length and get tail
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return head

        # Make it circular
        tail.next = head

        # Find new tail and head
        steps = length - k
        for _ in range(steps):
            tail = tail.next

        new_head = tail.next
        tail.next = None
        return new_head
