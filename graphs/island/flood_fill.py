"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

https://leetcode.com/problems/flood-fill/
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #Remember to check in the start if it given sr and sc is already at the new color
        if not image or image[sr][sc] == newColor: return image
        color= image[sr][sc]
        
        self.dfs(image, color, sr, sc, newColor)
        return image

    def dfs(self, image, color, sr, sc, newColor):
        if sr<0 or sc<0 or sr>=len(image) or sc>=len(image[0]) or image[sr][sc] != color:
            return

        image[sr][sc] = newColor
        self.dfs(image, color, sr+1, sc, newColor)
        self.dfs(image, color, sr-1, sc, newColor)
        self.dfs(image, color, sr, sc+1, newColor)
        self.dfs(image, color, sr, sc-1, newColor)
        return
        
