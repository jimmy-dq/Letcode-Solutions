#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/12/2 下午3:39
# @Author  : Jimmy_wqq
# @Site    : 
# @File    : 647_Palindromic_Substrings.py
# @Software: PyCharm Community Edition

class Solution:
   def force_countSubStrings(self, s):
       length = len(s)
       total = 0
       for i in  range(length):
           for j in  range(i, length):
               s_sub = s[i:j+1]
               if s_sub == s_sub[::-1]:
                  total += 1
       return total

   def extend_countSubstrings(self, s):
       """
       :type s: str
       :rtype: int
       """
       length = len(s)
       count = 0

       for i in range(length):
           # Odd
           left = i
           right = i
           while left > -1 and right < length and s[left] == s[right]:
               count += 1
               left -= 1
               right += 1
           # Even
           left = i
           right = i + 1
           while left > -1 and right < length and s[left] == s[right]:
               count += 1
               left -= 1
               right += 1
       return count

if __name__ == '__main__':
    s = Solution()
    total1 = s.force_countSubStrings('asdsdasdasdasdasdasdasdasdsa')
    total2 = s.extend_countSubstrings('asdsdasdasdasdasdasdasdasdsa')
    print total1
    print total2
