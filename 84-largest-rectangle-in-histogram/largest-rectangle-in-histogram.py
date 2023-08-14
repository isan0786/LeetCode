class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] #pair: (index, height)
        maxArea = 0


        for idx,height in enumerate(heights):
            start = idx
            while stack and stack[-1][1]>height:
                idx_stack,height_stack=stack.pop()
                maxArea = max(maxArea,(height_stack*(idx-idx_stack)))
                start = idx_stack
            stack.append((start,height))
        
        for idx,height in stack:
            maxArea = max(maxArea, (height*(len(heights)-idx)))

        return maxArea

        # this has a space complexity of O(N) and time complexity of O(N); because we are appending and removing len(heights) element from the stack