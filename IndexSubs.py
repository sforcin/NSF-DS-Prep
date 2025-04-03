'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 


'''
#Solution: 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        #we take the size of the needle, and then we use that as blocks to compare against the haystack
        for i in range(len(haystack) - len(needle) + 1): 
            match = True
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:  #compare the needle vs where we started in haystack
                    match = False
                    break
            if match:
                return i
        return -1  #if no match is found