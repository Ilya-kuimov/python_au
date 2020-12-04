# Array

+ [ Max Consecutive Ones](#max-consecutive-ones)
+ [ Reshape the Matrix](#reshape-the-matrix)
+ [ Image Smoother](#image-smoother)
+ [ Flipping an Image](#flipping-an-image)
+ [ Transpose Matrix](#transpose-matrix)
+ [ Move Zeroes](#move-zeroes)
+ [ Squares of a Sorted Array](#squares-of-a-sorted-array)

##  Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count_global = 0
        count_cur = 0
        for i in nums:
            if i == 1:
                count_cur += 1
            else:
                if count_cur > count_global:
                    count_global = count_cur
                count_cur = 0
        return max(count_global, count_cur)
```
##  Reshape the Matrix
https://leetcode.com/problems/reshape-the-matrix/
```python
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if r * c != len(nums) * len(nums[0]):
            return nums
        flatten = sum(nums, [])
        return [flatten[i*c:(i+1)*c] for i in range(r)]
```
##  Image Smoother
https://leetcode.com/problems/image-smoother/
```python
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        result = [[0]*n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                count = 0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if 0<=i<m and 0<=j<n:
                            result[r][c] += M[i][j]
                            count +=1
                result[r][c] = result[r][c]//count
        return result
```
##  Flipping an Image
https://leetcode.com/problems/flipping-an-image/
```python
class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1-val for val in row[::-1]] for row in A]
```
##  Transpose Matrix
https://leetcode.com/problems/transpose-matrix/
```python
class Solution:
    def matrixTranspose(anArray):
        transposed = [None]*len(anArray[0])

        for i in range(len(transposed)):
            transposed[i] = [None]*len(transposed)

        for t in range(len(anArray)):
            for tt in range(len(anArray[t])):            
                transposed[t][tt] = anArray[tt][t]
        return transposed

    theArray = [['a','b','c'],['d','e','f'],['g','h','i']]
    print matrixTranspose(theArray)
```
##  Move Zeroes
https://leetcode.com/problems/move-zeroes/
```python
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        point = 0
        for i in range(len(nums)):
            if nums[point]:
                point += 1
            elif nums[i]:
                nums[point], nums[i] = nums[i], 0
                point += 1
```
##  Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = []
        for number in A:
            B.append(number * number)
        return sorted(B)
```