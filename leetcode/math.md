# Math

+ [ Reverse Integer](#reverse-integer)
+ [ Palindrome Number](#palindrome-number)
+ [ Fizz Buzz](#fizz-buzz)
+ [ Base 7](#base-7)
+ [ Fibonacci Number](#fibonacci-number)
+ [ Largest Perimeter Triangle](#largest-perimeter-triangle)
+ [ Sqrt(x)](#sqrtx)

##  Reverse Integer
https://leetcode.com/problems/reverse-integer/
```python
class Solution:
    def reverse(self, x: int) -> int:
        isNegative = x < 0
        x = abs(x)
        reversed = 0        
 
        while x != 0:
            reversed = reversed * 10 + x % 10
            x //= 10
 
        if reversed > 2**31 - 1:
            return 0
        else:
            return reversed if not isNegative else -reversed
```
##  Palindrome Number
https://leetcode.com/problems/palindrome-number/
```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = len(str(x)) // 2
 
        if len(str(x)) % 2 != 0:
            n = len(str(x)) // 2
            return str(x)[:n] == str(x)[:n:-1]
        elif len(str(x)) % 2 == 0:
            return str(x)[:n] == str(x)[n:][::-1]
        else:
            return False
```
##  Fizz Buzz
https://leetcode.com/problems/fizz-buzz/
```python
class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def func(num):
            if num % 15 == 0:
                return "FizzBuzz"
            if num % 3 == 0:
                return "Fizz"
            if num % 5 == 0:
                return "Buzz"
            return str(num)
        
        return [func(num) for num in range(1, n+1)]
```
##  Base 7
https://leetcode.com/problems/base-7/
```python
class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return str(num)
        n = abs(num)
        res = ""
        while n:
            res = str(n%7)+res
            n = n//7
        return res if num > 0 else "-"+res
```
##  Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
```python
class Solution {
public:
    int fib(int N) {
        if (N <= 1) return N;
        int a = 0, b = 1;
        for (int i = 2; i <= N; ++i) {
            int sum = a + b;
            a = b;
            b = sum;
        }
        return b;
    }
};
```
##  Largest Perimeter Triangle
https://leetcode.com/problems/largest-perimeter-triangle/
```python
class Solution {
    public int largestPerimeter(int[] A) {
        Arrays.sort(A);
        int L = A.length;
        for (int i = L - 1; i >= 2; i--) {
            int a = A[i-2];
            int b = A[i-1];
            int c = A[i];
            if (c < a + b) {
                return a + b + c;
            }
        }
        return 0;
    }
}
```
##  Sqrt(x)
https://leetcode.com/problems/sqrtx/
```python
class Solution:
    def mySqrt(self, x):
        """
        rtype x: int
        iptype: int
        """
        result = x
        while not result * result - x < 1:
            result = (result + x / result) / 2

        return int(result)
```