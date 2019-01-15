#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19/1/15 下午3:19
# @Author  : Jimmy_wqq
# @Site    : 
# @File    : ToeplitzMatrix.py
# @Software: PyCharm Community Edition

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(1, len(matrix)):
            if matrix[i][1:] != matrix[i - 1][:-1]:
                return False
        return True

if __name__ == '__main__':
     s = Solution()
     print s.isToeplitzMatrix([[1,2,3,5],[5,1,2,3],[9,5,1,2]])