#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
5. Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
"""


class Solution(object):
    def longestPalindrome(self, s, method='a'):
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

        if len(s) == 0:
            return 0

        start = 0
        max_len = 1

        for i in range(len(s)):
            if i - max_len >= 1 and s[i - max_len - 1:i + 1] == s[i - max_len - 1:i + 1][::-1]:
                start = i - max_len - 1
                max_len += 2
                continue

            if i - max_len >= 0 and s[i - max_len:i + 1] == s[i - max_len:i + 1][::-1]:
                start = i - max_len
                max_len += 1

        return s[start:start + max_len]

    @staticmethod
    def b(s):
        """
        :param s: str
        :return: str
        """

        _len = len(s)
        if _len <= 1:
            return s

        min_start, max_len, i = 0, 1, 0

        while i < _len:
            if _len - i <= max_len / 2:
                break

            j, k = i, i

            while k < _len - 1 and s[k] == s[k + 1]:
                k += 1

            i = k + 1

            while k < _len - 1 and j and s[k + 1] == s[j - 1]:
                k, j = k + 1, j - 1

            if k - j + 1 > max_len:
                min_start, max_len = j, k - j + 1

        return s[min_start: min_start + max_len]

    @staticmethod
    def c(s):
        """
        Manacher's algorithm: https://en.wikipedia.org/wiki/Longest_palindromic_substring

        Transform s into t.
        For example, s = "abba", t = "^#a#b#b#a#$".
        ^ and $ signs are sentinels appended to each end to avoid bounds checking

        :param s: str
        :return: str
        """

        t = '#'.join('^{}$'.format(s))
        n = len(t)
        p = [0] * n
        c = r = 0

        for i in range(1, n - 1):
            p[i] = (r > i) and min(r - i, p[2 * c - i])  # equals to i' = c - (i - c)
            # Attempt to expand palindrome centered at i
            while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
                p[i] += 1

            # If palindrome centered at i expand past r,
            # adjust center based on expanded palindrome.
            if i + p[i] > r:
                c, r = i, i + p[i]

        # Find the maximum element in p.
        max_len, center_index = max((n, i) for i, n in enumerate(p))

        return s[(center_index - max_len) // 2: (center_index + max_len) // 2]

    @staticmethod
    def d(s):
        """
        :param s: str
        :return: str
        """

        def _helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        result = ''

        for i in range(len(s)):
            for k in range(2):
                tmp = _helper(s, i, i + k)
                if len(tmp) > len(result):
                    result = tmp

        return result


if __name__ == '__main__':
    solution = Solution()

    for _s in ['sdklslevelsdfksll', 'slfkdslaaabbaaaslfkwok']:
        ret = solution.longestPalindrome(s=_s)
        print(_s, '==>', ret)
