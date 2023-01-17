class Solution(object):
    def lengthOfLongestSubstring(self, s: str):
        longest = ''
        flongest = ''
        size = 0
        for val in s:
            if val in longest:
                #size = len(longest)
                if len(longest) > len(flongest):
                    flongest = longest
                    size = len(longest)

                longest = '' + val
            else:
                longest += val
        if len(longest) > len(flongest):
            flongest = longest
            size = len(flongest)

        return (flongest, size)


c1 = Solution()
c2 = Solution()
c3 = Solution()

print(c1.lengthOfLongestSubstring('abcabcdabcdef')) # returns ('abcdef', 6)
print(c2.lengthOfLongestSubstring('bbbbb')) # returns ('b', 1)
print(c3.lengthOfLongestSubstring('pwwkew')) # returns ('wke', 3)
