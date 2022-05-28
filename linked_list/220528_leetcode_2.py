# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, node: ListNode = None):
        self.head = node

    def add_node(self, node: ListNode):
        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def get_all(self):
        all = []
        if self.head is None:
            return all

        current = self.head

        while current:
            all.append(current.value)
            current = current.next

        return all


class Solution:
    def getReversedNum(self, l: LinkedList):
        reversed_all = reversed(l.get_all())
        return int(''.join(map(lambda x: str(x), reversed_all)))

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list_one, list_two = LinkedList(), LinkedList()

        for node in l1:
            list_one.add_node(ListNode(node))

        for node in l2:
            list_two.add_node(ListNode(node))

        added = self.getReversedNum(list_one) + self.getReversedNum(list_two)

        ret = list(map(lambda x: int(x), str(added)))
        ret.reverse()
        return ret


s = Solution()

print(s.addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4]))
print(s.addTwoNumbers(l1=[0], l2=[0]))
print(s.addTwoNumbers(l1=[9,9,9,9,9,9,9], l2=[9,9,9,9]))
