# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        max_path = {}
        stack = [root]

        while stack:
            node = stack[-1]

            if node.left and node.left not in max_path:
                stack.append(node.left)
            elif node.right and node.right not in max_path:
                stack.append(node.right)
            else:
                node = stack.pop()
                leftMax = max(max_path.get(node.left, 0), 0)
                rightMax = max(max_path.get(node.right, 0), 0)
                res = max(res, node.val + leftMax + rightMax)
                max_path[node] = node.val + max(leftMax, rightMax)
        
        return res
