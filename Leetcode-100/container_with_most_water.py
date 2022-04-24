class Solution:
    def maxArea(self, height):
        start = 0
        end = len(height)-1
        largest = 0
        # prev_start = 0
        # prev_end = 0
        while start!=end:
            # if height[start]<prev_start:
            #     start+=1
            #     continue
            # if height[end]<prev_end:
            #     end-=1
            #     continue
            area = min(height[end], height[start])*(end-start)
            if area > largest:
                largest = area
            if height[start]<height[end]:
                # prev_start = height[start]
                start+=1
            else:
                # prev_end = height[end]
                end-=1
        return largest