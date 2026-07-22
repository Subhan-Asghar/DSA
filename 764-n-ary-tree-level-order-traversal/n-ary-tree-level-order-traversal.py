"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q=deque([root])
        result=[]
        while q:
            n=len(q)
            level=[]
            for _ in range(n):
                node=q.popleft()
                level.append(node.val)           
                for nei in node.children:
                    q.append(nei)
            result.append(level)
        return result 