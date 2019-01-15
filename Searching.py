#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/12/8 下午2:23
# @Author  : Jimmy_wqq
# @Site    : 
# @File    : Searching.py
# @Software: PyCharm Community Edition

class Searching_algorithms:
    # 快速排序
    # 通过一趟排序将要排序的数据分割成独立的两部分
    # 其中一部分的所有数据都比另外一部分的所有数据都要小
    # 然后再按此方法对这两部分数据分别进行快速排序
    # 整个排序过程可以递归进行
    # 以此达到整个数据变成有序序列。
    def quick_sort(self, num_list):
        less = []
        pivotList = []
        more = []
        if len(num_list)<= 1:
            return num_list
        else:
            pivot = num_list[0]
            for i in num_list:
                if i < pivot:
                    less.append(i)
                elif i>pivot:
                    more.append(i)
                else:
                    pivotList.append(i)
            less = self.quick_sort(less)
            more = self.quick_sort(more)
            return more+pivotList+less



    # 将数字插入致已排序好的list中
    def insert_search(self, num_list):
        if len(num_list) == 1:
            return num_list
        else:
            for i in range(1, len(num_list)):
                temp = num_list[i]
                for j in range(i):
                    if temp > num_list[j]:
                        for k in range(i, j, -1):
                            num_list[k] = num_list[k-1]
                        num_list[j] = temp
                        break
            return num_list

    # 冒泡排序
    # 比较相邻的元素大小，将小的前移，大的后移，就像水中的气泡一样，最小的元素经过几次移动，会最终浮到水面上。
    def pop_search(self, num_list):
        if len(num_list) == 1:
            return num_list
        else:
            for i in range(len(num_list)):
                for j in range(len(num_list)-i-1):
                    if num_list[j] > num_list[j+1]:
                        temp = num_list[j]
                        num_list[j] = num_list[j+1]
                        num_list[j+1] = temp
            return num_list

if __name__ == '__main__':
    s = Searching_algorithms()
    num_list = [1,3,2,6,4,8,7,3,2]
    # num_list = s.pop_search(num_list)
    # num_list = s.insert_search(num_list)
    num_list = s.quick_sort(num_list)
    print num_list