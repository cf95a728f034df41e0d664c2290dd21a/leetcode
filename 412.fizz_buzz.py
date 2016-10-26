#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
412. Fizz Buzz

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""

import json


class Solution(object):
    def fizzBuzz(self, n, method='a'):
        _method = getattr(self, method)
        if not _method:
            raise Exception('Method `{}` not found.'.format(method))

        return _method(n=n)

    @staticmethod
    def a(n):
        """
        :param n: int
        :return: list[str]
        """

        results = []

        for i in range(1, n + 1):
            c = ''

            if i % 3 == 0:
                c += 'Fizz'
            if i % 5 == 0:
                c += 'Buzz'

            if not c:
                c = str(i)

            results.append(c)

        return results


if __name__ == '__main__':
    solution = Solution()
    ret = solution.fizzBuzz(15)
    print(json.dumps(obj=ret, indent='\t'))
