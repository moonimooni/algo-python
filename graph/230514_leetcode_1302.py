# https://leetcode.com/problems/deepest-leaves-sum/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    __node_depth = 0
    __deepest_nodes_sum = 0

    def __is_deepest_node(self, node: TreeNode, current_depth) -> bool:
        return node.left is None and node.right is None and current_depth == self.__node_depth

    def __dfs(self, node: TreeNode, depth):

        if node.val == None:
            return

        if depth > self.__node_depth:
            self.__node_depth = depth
            # deepest nodes sum 값이 있는데 더 깊은 노드가 발견되면 sum 값 초기화
            if self.__deepest_nodes_sum is not 0:
                self.__deepest_nodes_sum = 0

        if self.__is_deepest_node(node, depth):
            self.__deepest_nodes_sum += node.val

        depth += 1

        if node.left:
            self.__dfs(node.left, depth)
        if node.right:
            self.__dfs(node.right, depth)

        return

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.__dfs(root, 0)
        return self.__deepest_nodes_sum
