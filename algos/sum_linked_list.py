from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def convert_to_list(node):
            lst = []
            current = node
            while True and node:
                lst.append(current.val)
                if current.next:
                    current = current.next
                else:
                    break
            else:
                return [0]
            return lst

        l1 = convert_to_list(l1)
        l2 = convert_to_list(l2)
        l3 = []

        ln1 = len(l1)
        ln2 = len(l2)

        car = 0
        for i in range(max([ln1, ln2])):
            x = l1[i] if i < ln1 else 0
            y = l2[i] if i < ln2 else 0

            sum_ = x + y + car

            if sum_ > 9:
                l3.append(sum_ % 10)
                car = 1
            else:
                l3.append(sum_)
                car = 0
        if car:
            l3.append(1)

        head = None
        prev = None
        for l in l3:
            if not prev:
                head = ListNode(l)
                prev = head
            else:
                node = ListNode(l)
                prev.next = node
                prev = node

        return head
