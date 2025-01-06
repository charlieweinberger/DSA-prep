# https://leetcode.com/problems/container-with-most-water

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:

            currentHeight = min(height[left], height[right])
            currentWidth = right - left
            currentArea = currentHeight * currentWidth

            if maxArea < currentArea:
                maxArea = currentArea

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea