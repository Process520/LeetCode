#-*- coding: utf-8 -*-
# python2.7
# Name: Two Sum
# Author: Process
# Adress: USTC
# Date: Thursday, 5th April, 2018
class Solution(object):
    def twoSum(self, nums, target):
        a = sorted(nums)
        low = 0
        high = len(nums) - 1
        while low < high:
            sum = a[low] + a[high]
            if target == sum:   
                index1 = 0
                while index1 <= len(nums)-1:
                    if a[low] == nums[index1]:
                        break
                    else:
                        index1 = index1+1
                index2 = len(nums) - 1 
                while index2 >= 0:
                    if a[high] == nums[index2]:
                        break
                    else:
                        index2 = index2-1                       
                return [index1, index2]
            elif target > sum:
                high = high -1
            elif target < sum:
                low  = low + 1
s = Solution()
print s.twoSum([3,2,3],6)
