# <!-- Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces. -->

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # set because we want unique vals
        L = 0 # left pointer start
        res = 0 #result initialize & declare

        #our right pointer is going to be moving each iteration so writing a for loop
        for R in range(len(s)):
          
            while s[R] in charSet: #we want to find out if the value exist in set
                charSet.remove(s[L]) #we remove the left pointer value 
                L += 1 #increment left pointer to next
                print(R-L) #I wrote this to figure out why we need +1 later
            charSet.add(s[R]) #once the loop breaks we add the new unique R pointer value
            res = max(res, (R - L) + 1 ) # result is max of result and right pointer - left pointer val
        return res #returning the count of sliding window calculated from line 15