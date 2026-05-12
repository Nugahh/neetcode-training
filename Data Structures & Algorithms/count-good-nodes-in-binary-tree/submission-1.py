# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = root.val
        queue = deque([(root, maxVal)])

        count = 1
        while queue:
            for i in range(len(queue)):
                node, maxVal = queue.popleft()
                if node.left:
                    queue.append((node.left, max(maxVal, node.left.val)))
                    if node.left.val >= maxVal:
                        count += 1
                if node.right:
                    queue.append((node.right, max(maxVal, node.right.val)))
                    if node.right.val >= maxVal:
                        count += 1
                
        return count
