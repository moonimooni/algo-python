# https://leetcode.com/problems/reverse-linked-list/
from copy import deepcopy
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous_node = None
        current_node = deepcopy(head)

        while current_node is not None:
            next, current_node.next = current_node.next, previous_node
            previous_node = current_node
            current_node = next

        current_node = previous_node
        return current_node
