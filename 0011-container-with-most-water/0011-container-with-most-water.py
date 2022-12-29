class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0
        
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            print(left, right)
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area