'''Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.You can return the answer in any order.'''
from typing import List


class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        numMap = {}
        n =len(num)

        for i in range(n):
            complement = target -num[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]

        return []
