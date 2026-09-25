class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0  # track global max diameter

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = height(node.left)
            right = height(node.right)

            # Diameter through this node
            self.diameter = max(self.diameter, left + right)

            # Return height to parent
            return 1 + max(left, right)

        height(root)
        return self.diameter