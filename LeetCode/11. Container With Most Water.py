from typing import List

def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    maxWater = 0

    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        water = width * min_height
        maxWater = max(maxWater, water)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxWater