import bisect

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = (len(matrix) * len(matrix[0]))-1

        

        # bisect.bisect_left()

        while (l <= r):
            m = (r+l) // 2

            row = m // len(matrix[0])
            col = m % len(matrix[0])

            if matrix[row][col] < target:
                l = m+1
            elif matrix[row][col] > target:
                r = m-1
            else: return True
        return False
