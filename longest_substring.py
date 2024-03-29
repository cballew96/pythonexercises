class Solution(object):
    def lengthOfLongestSubstring(self, s: str):
        start = 0
        index = 1
        longest = ''
        flongest = ''
        size = 0
        while start < len(s):
            if s[start] in longest:
                start = index
                index += 1
                #size = len(longest)
                if len(longest) > len(flongest):
                    flongest = longest
                    size = len(longest)

                longest = '' + s[start]

            else:
                longest += s[start]
            start += 1
        if len(longest) > len(flongest):
            flongest = longest
            size = len(flongest)

        return (flongest, size)

c1 = Solution()
c2 = Solution()
c3 = Solution()
c4 = Solution()

print(c1.lengthOfLongestSubstring('abcabcdabcdef')) # returns ('abcdef', 6)
print(c2.lengthOfLongestSubstring('bbbbb')) # returns ('b', 1)
print(c3.lengthOfLongestSubstring('pwwkew')) # returns ('wke', 3)
print(c4.lengthOfLongestSubstring('dvdf')) # returns ('vdf', 3)
