from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        final  = []
        q = deque()
        q.append(root)
        while(q):
            cur_level = []
            for _ in range(len(q)):
                u = q.popleft()
                if(u.left):
                    q.append(u.left)
                if(u.right):
                    q.append(u.right)
                cur_level.append(u.val)
            final.append(cur_level)
        return final
