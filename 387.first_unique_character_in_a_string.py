#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
"""


class Solution(object):
    def firstUniqChar(self, s, method='a'):
        _method = getattr(self, method)
        if not _method:
            raise Exception('Method `{}` not found.'.format(method))

        return _method(s=s)

    @staticmethod
    def a(s):
        """
        :param s: str
        :return: int
        """

        _d = {}
        for i, c in enumerate(s):
            if c in _d:
                _d[c].append(i)
            else:
                _d[c] = [i]

        _l = [v[0] for k, v in _d.items() if len(v) == 1]

        return sorted(_l)[0] if _l else -1


if __name__ == '__main__':
    solution = Solution()

    for _s in ['leetcode', 'loveleetcode']:
        result = solution.firstUniqChar(s=_s)
        print(_s, '==>', result)
