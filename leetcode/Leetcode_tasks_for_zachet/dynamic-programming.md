# Dynamic programming

+ [ House Robber II](#house-robber-ii)
+ [ House Robber](#house-robber)

##  House Robber II
https://leetcode.com/problems/house-robber-ii/
```python
public class Solution {
    public int rob(int[] num) {
        if (num.length == 0)
            return 0;
        else if (num.length == 1)
            return num[0];
        else
            return Math.max(robRange(num, 0, num.length - 2), robRange(num, 1, num.length -1));
    }
    private int robRange(int[] num, int start, int end){
        int with = num[start];
        int without = 0;
        for (int i = start + 1; i <= end; i ++){
            int newWith = without + num[i];
            int newWithout = Math.max(with, without);
            with = newWith;
            without = newWithout;
        }
        return Math.max(with, without);
    }
}
```
##  House Robber
https://leetcode.com/problems/house-robber/
```python
class Solution:
    def rob(self, nums):
        """
        DP
        O(n)
        Let F_i be max value END AT or BEFORE i
        F_i = max(F_{i-1}, F_{i-2} + A[i])
        Notes:
        If change the definition of F_i
        Let F_i be mex value END AT i
        F_i = max(F_{i-2-k}+A[i] for k \in [0, i-2]),
        Then time complexity is quadratic
        """
        n = len(nums)
        f = [0 for _ in xrange(n+2)]
        for i in xrange(2, n+2):
            f[i] = max(
                f[i-1],
                f[i-2] + nums[i-2]
            )

        return f[-1]
```