#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/12/5 下午10:32
# @Author  : Jimmy_wqq
# @Site    : 
# @File    : 147_Insertion_Sort_List.py
# @Software: PyCharm Community Edition

class Solution:
    def sort_arrays(self, head):
        for i in range(len(head)):
            if i == 0:
                continue
            current_value = head[i]
            for j in range(i,0,-1):
                if head[j-1] > current_value:
                    head[j] = head[j-1]
                    if j-1 == 0 or head[j-2] <= current_value:
                        head[j-1] = current_value
                else:
                    break
        return head

if __name__ == '__main__':
    s = Solution()
    arrasy = s.sort_arrays([13,2,4,6,5])
    print arrasy