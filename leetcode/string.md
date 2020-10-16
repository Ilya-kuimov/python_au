# String

+ [ Reverse String](#reverse-string)
+ [ Valid Anagram](#valid-anagram)
+ [ Reverse Vowels of a String](#reverse-vowels-of-a-string)

##  Reverse String
https://leetcode.com/problems/reverse-string/
```python
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)
```
##  Valid Anagram
https://leetcode.com/problems/valid-anagram/
```python
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        counter = dict()
        for c in s:
            counter[c] = counter.get(c, 0) + 1
        for c in t:
            if not counter.get(c, 0):
                return False
            counter[c] -= 1
        return sum(counter.values()) == 0
```
##  Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
```python
class Solution:
   def reverseVowels(self, s):
      chars = list(s)
      index = []
      vowels = []
      for i in range(len(chars)):
         if chars[i] in ['a','e','i','o','u']:
         vowels.append(chars[i])
         index.append(i)
      vowels = vowels[::-1]
      final = []
      ind = 0
      for i in range(len(chars)):
      if i in index:
         final.append(vowels[ind])
         ind += 1
      else:
         final.append(chars[i])
   str1 = ""
   return str1.join(final)
ob1 = Solution()
print(ob1.reverseVowels("hello"))
print(ob1.reverseVowels("programming"))
```
