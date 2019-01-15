#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/12/2 下午1:06
# @Author  : Jimmy_wqq
# @Site    : 
# @File    : 338_counting_bits.py
# @Software: PyCharm Community Edition

class Solution:
    def CountBits(self, num):
        """
                :type num: int
                :rtype: List[int]
                """

        ans = [0] + [None for _ in range(num)]

        for i in range(1, num + 1):
            ans[i] = ans[i & i - 1] + 1

        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.CountBits(10)
    print res