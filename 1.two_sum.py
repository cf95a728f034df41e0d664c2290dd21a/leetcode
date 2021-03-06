#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

import copy
import random
from datetime import datetime


class Solution(object):
    def twoSum(self, nums, target, method='a'):
        _method = getattr(self, method)
        if not _method:
            raise Exception('Method `{}` not found.'.format(method))

        return _method(nums=nums, target=target)

    @staticmethod
    def a(nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: list[int]
        """

        _buffer = {}

        for i in range(len(nums)):
            if nums[i] in _buffer:
                return [_buffer[nums[i]], i]
            else:
                _buffer[target - nums[i]] = i

        return [-1, -1]

    @staticmethod
    def b(nums, target):
        """
        :param nums: list[int]
        :param target: int
        :return: list[int]
        """

        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:]):
                if a + b == target:
                    return [i, i + j + 1]

        return [-1, -1]


if __name__ == '__main__':
    solution = Solution()

    _target = 9
    _nums = [2, 7, 11, 15]

    for index in range(100):
        temp = copy.deepcopy(_nums)
        random.shuffle(temp)

        dt1 = datetime.now()
        results = solution.twoSum(nums=temp, target=9)
        dt2 = datetime.now()

        print('%03d' % index, '\t', temp, '\t', results, '\t', '%0.3fms' % ((dt2 - dt1).microseconds / 1000))
