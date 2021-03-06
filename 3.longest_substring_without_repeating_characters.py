#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s, method='a'):
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

        start = max_length = 0
        used_char = {}

        for index in range(len(s)):
            if s[index] in used_char and start <= used_char[s[index]]:
                start = used_char[s[index]] + 1
            else:
                max_length = max(max_length, index - start + 1)

            used_char[s[index]] = index

        return max_length

    @staticmethod
    def b(s):
        """
        :param s: str
        :return: int
        """

        if not s:
            return 0

        i, j, m, n = 0, 0, 0, len(s)

        while j < n:
            if s[j] not in s[i:j]:
                j += 1
                m = max(m, j - i)
            else:
                i += 1

        return m


if __name__ == '__main__':
    # http://www.cnblogs.com/Erdos001/p/5820668.html

    solution = Solution()

    for _s in ['abcabcbb', 'bbbbb', 'pwwkew']:
        print(_s, '\t', solution.lengthOfLongestSubstring(s=_s))
