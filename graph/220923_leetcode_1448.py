# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ret: int = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, root.val)
        return self.ret

    def dfs(self, node: TreeNode, greatest_num: int):
        # null이 어떻게 들어오는겨? None?
        if type(node) is None:
            return
        if node.val >= greatest_num:
            self.ret += 1
            greatest_num = node.val
        if node.left is not None:
            self.dfs(node.left, greatest_num)
        if node.right is not None:
            self.dfs(node.right, greatest_num)

        return
