# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def recursive(node):
            nonlocal cnt,res
            if not node: return
            
            recursive(node.left)
            cnt -= 1

            if cnt == 0:
                res = node.val
                return

            recursive(node.right)

        recursive(root)
        return res
        