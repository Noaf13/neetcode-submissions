class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix [0])
        t = r*c

        L,R = 0,t-1

        while L<= R:
            m = (L+R)//2
            if matrix[m//c][m%c] == target:
                return True

            elif matrix[m//c][m%c] < target:
                L = m + 1

            elif matrix[m//c][m%c] > target:
                R = m -1
        return False

        