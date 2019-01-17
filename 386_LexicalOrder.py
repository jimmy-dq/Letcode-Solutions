#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 19/1/17 下午10:13
# @Author  : Jimmy_wqq
# @Site    : 
# @File    : 386_LexicalOrder.py DFS Solution: https://leetcode.com/problems/lexicographical-numbers/discuss/86231/simple-java-dfs-solution
# @Software: PyCharm Community Edition

class lexicalOrder:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(1, 10, 1):
            self.dfs(i, n, res)
        return res

    def dfs(self, cur, n ,res):
        if(cur>n):
            return
        else:
            res.append(cur)
            for j in range(10):
                if(10*cur+j>n):
                    return
                self.dfs(10*cur+j, n, res)

if __name__ == '__main__':
    l = lexicalOrder()
    print l.lexicalOrder(13)