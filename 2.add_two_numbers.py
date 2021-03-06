#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
2. Add Two Numbers

You are given two linked lists representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


class ListNode(object):
    """
    singly-linked list
    """

    def __init__(self, val, next=None):
        """
        :param val: any
        :param next: ListNode
        """

        self.val = val
        self.next = next

    @staticmethod
    def to_list(node):
        """
        :param node: ListNode
        :return: list
        """

        while True:
            yield node.val

            if not node.next:
                break

            node = node.next

    @staticmethod
    def from_list(items):
        """
        :param items: list
        :return node: ListNode
        """

        node = None
        for item in items[::-1]:
            node = ListNode(val=item, next=node)

        return node

    def __repr__(self):
        return '({})'.format(' -> '.join([str(item) for item in self.to_list(node=self)]))


class Solution(object):
    def addTwoNumbers(self, l1, l2, method='a'):
        _method = getattr(self, method)
        if not _method:
            raise Exception('Method `{}` not found.'.format(method))

        return _method(l1=l1, l2=l2)

    @staticmethod
    def a(l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        """

        carry = 0
        result = node = ListNode(0)

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next

            if l2:
                carry += l2.val
                l2 = l2.next

            carry, val = divmod(carry, 10)
            node.next = node = ListNode(val)

        return result.next


if __name__ == '__main__':
    solution = Solution()

    _l1 = ListNode.from_list([2, 4, 3])
    _l2 = ListNode.from_list([5, 6, 4])

    _l3 = solution.addTwoNumbers(l1=_l1, l2=_l2)
    print(str(_l1), '+', str(_l2), '=', str(_l3))
