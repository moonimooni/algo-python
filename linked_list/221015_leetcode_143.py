# https://leetcode.com/problems/reorder-list/

from copy import deepcopy
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first_half_head, second_half_head = self.__split_list(head)
        reversed_second_half_head = self.__reverse_list(second_half_head)

        ret = None

        while first_half_head:
            # add first half head
            if ret is None:
                ret = first_half_head
                node_pointer = ret
            else:
                node_pointer.next = first_half_head
                node_pointer = node_pointer.next

            first_half_head = first_half_head.next

            # add second half half
            node_pointer.next = reversed_second_half_head
            reversed_second_half_head = reversed_second_half_head.next if reversed_second_half_head else None

            node_pointer = node_pointer.next
        
        return ret

    def __split_list(self, head: ListNode):
        copied_head = deepcopy(head)
        # tortoise and hare
        slow = copied_head
        fast = copied_head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle_node = slow.next
        slow.next = None

        return copied_head, middle_node

    def __reverse_list(self, head: ListNode) -> ListNode:
        previous_node = None
        current_node = deepcopy(head)

        while current_node is not None:
            next, current_node.next = current_node.next, previous_node
            previous_node = current_node
            current_node = next

        current_node = previous_node
        return current_node
