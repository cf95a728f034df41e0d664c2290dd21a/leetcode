#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
344. Reverse String

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""


class Solution(object):
    def reverseString(self, s, method='a'):
        _method = getattr(self, method)
        if not _method:
            raise Exception('Method `{}` not found.'.format(method))

        return _method(s=s)

    @staticmethod
    def a(s):
        """
        :param s: str
        :return: str
        """

        return s[::-1]


if __name__ == '__main__':
    solution = Solution()

    _input = 'hello'
    _output = solution.reverseString(s='hello')

    print(_input, '==>', _output)
