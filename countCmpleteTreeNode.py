class Solution(object):
    def countNodes(self, root):
        def getHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        if not root:
            return 0

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        if left_height == right_height:
            # Left subtree is perfect
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is perfect
            return (1 << right_height) + self.countNodes(root.left)
