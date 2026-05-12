# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSametree(self, root, subRoot) -> bool:
        queue = deque([(root, subRoot)])

        while queue:
            node, nodeSub = queue.popleft()

            if not node and not nodeSub:
                continue
            if not node or not nodeSub or node.val != nodeSub.val:
                return False
            
            queue.append((node.left, nodeSub.left))
            queue.append((node.right, nodeSub.right))

        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root:
            return False
            
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                continue
            if self.isSametree(node, subRoot):
                return True
            queue.append(node.left)
            queue.append(node.right)
        return False