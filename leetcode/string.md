# String

+ [ Reverse String](#reverse-string)
+ [ Valid Anagram](#valid-anagram)
+ [ Reverse Vowels of a String](#reverse-vowels-of-a-string)
+ [ Reverse Words in a String III](#reverse-words-in-a-string-iii)
+ [ To Lower Case](#to-lower-case)

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
##  Reverse Words in a String III
https://leetcode.com/problems/reverse-words-in-a-string-iii/
```python
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([word[::-1] for word in s.split(' ')]
```
##  To Lower Case
https://leetcode.com/problems/to-lower-case/
```python
var toLowerCase = function(str) {
  // let result = [];
  var result = ``;

  str.split('').forEach(char => {
    // find current position
    let current = char.charCodeAt(0);

    if ('A'.charCodeAt(0) <= current) {
      if (current <= 'Z'.charCodeAt(0)) {
        let next = current - 'A'.charCodeAt(0);
        let newCharIndex = 'a'.charCodeAt(0) + next;
        let newChar = String.fromCharCode(newCharIndex);

        result = result + newChar;
      } else {
        result = result + char;
      }
    } else {
      result = result + char;
    }
  });
  return result;
};

module.exports = {
  toLowerCase
}
```