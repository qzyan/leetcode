class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        water = 0
        for idx in range(len(height)):
            curr_h = height[idx]
            while stack and height[stack[-1]] <= curr_h:
                min_h = height[stack.pop()]
                if not stack:
                    continue

                bound_h = min(curr_h, height[stack[-1]])
                water += (bound_h - min_h) * (idx - stack[-1] - 1)
            
            stack.append(idx)

        return water

