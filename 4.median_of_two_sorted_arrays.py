#! /usr/bin/python
# -*- coding: utf-8 -*-


"""
4. Median of Two Sorted Arrays

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2, method='a'):
        _method = getattr(self, method)
        if not _method:
            raise Exception('Method `{}` not found.'.format(method))

        return _method(nums1=nums1, nums2=nums2)

    def a(self, nums1, nums2):
        """
        :param nums1: list[int]
        :param nums2: list[int]
        :return: float
        """

        _len = len(nums1) + len(nums2)
        if _len % 2 == 1:
            return self._kth(nums1, nums2, _len // 2)
        else:
            return (self._kth(nums1, nums2, _len // 2 - 1) + self._kth(nums1, nums2, _len // 2)) / 2.0

    def _kth(self, nums1, nums2, k):
        """
        :param nums1: list[int]
        :param nums2: list[int]
        :param k: int
        :return: float
        """

        if not nums1:
            return nums2[k]

        if not nums2:
            return nums1[k]

        index1, index2 = len(nums1) // 2, len(nums2) // 2
        num1, num2 = nums1[index1], nums2[index2]

        # when k is bigger than the sum of nums1 and nums2's median indices 
        if index1 + index2 < k:
            # if nums1's median is bigger than nums2's, nums2's first half doesn't include k
            if num1 > num2:
                return self._kth(nums1, nums2[index2 + 1:], k - index2 - 1)
            else:
                return self._kth(nums1[index1 + 1:], nums2, k - index1 - 1)
        # when k is smaller than the sum of nums1 and nums2's indices
        else:
            # if nums1's median is bigger than nums2's, nums1's second half doesn't include k
            if num1 > num2:
                return self._kth(nums1[:index1], nums2, k)
            else:
                return self._kth(nums1, nums2[:index2], k)


if __name__ == '__main__':
    solution = Solution()

    ret = solution.findMedianSortedArrays(nums1=[1, 3], nums2=[2])
    print(ret)

    ret = solution.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])
    print(ret)
