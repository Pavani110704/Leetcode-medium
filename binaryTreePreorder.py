class Solution(object):
    def preorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val)    # Visit root
            dfs(node.left)             # Traverse left
            dfs(node.right)            # Traverse right
        
        dfs(root)
        return result
