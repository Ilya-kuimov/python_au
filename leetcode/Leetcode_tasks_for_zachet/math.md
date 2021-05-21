# Math

+ [ K Closest Points to Origin](#k-closest-points-to-origin)

##  K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
```python
class Solution:
  def kClosest(self, points, K):
    return sorted(points, key = lambda p: p[0]**2 + p[1]**2)[0:K]
```