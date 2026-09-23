from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        depth = 0

        if not root:
            return 0

        while q:

            nodes_in_level = len(q)

            for _ in range (nodes_in_level):

                self.root = q.popleft()

                if self.root.left: q.append(self.root.left)
                if self.root.right: q.append(self.root.right)
            depth +=1
        
        return depth

        
        