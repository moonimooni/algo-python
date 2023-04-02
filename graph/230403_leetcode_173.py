# https://leetcode.com/problems/binary-search-tree-iterator/

from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    nodes_in_asc_order = []
    idx = -1

    def __init__(self, root: Optional[TreeNode]):
        self.nodes_in_asc_order = self.__get_bst_vals_only(root, [])
        self.nodes_in_asc_order.sort()
        self.nodes_in_asc_order = [{
            'val': x,
            'right': self.nodes_in_asc_order[i+1] if i+1 < len(self.nodes_in_asc_order) else None
        } for i, x in enumerate(self.nodes_in_asc_order)]

    def __get_bst_vals_only(self, root, nodes):
        if not root:
            return

        nodes.append(root.val)

        self.__get_bst_vals_only(root.left, nodes)
        self.__get_bst_vals_only(root.right, nodes)

        return nodes

    def next(self) -> int:
        self.idx += 1
        return self.nodes_in_asc_order[self.idx]['val']

    def hasNext(self) -> bool:
        return True if self.nodes_in_asc_order[self.idx]['right'] or self.idx == -1 else False
