# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count=0
        def func(node):
            nonlocal count
            if not node:
                return 0
            if not node.left and not node.right:
                count+=1
                return node.val

            left=func(node.left)
            right=func(node.right)
            max_val=max(left,right,node.val)
            if max_val==node.val:
                count+=1
            return max_val
        func(root)
        return count

