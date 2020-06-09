class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        s_length = len(s)

        for letter in t:
            if letter == s[i]:
                i += 1
            if i == s_length:
                return True

        return False

# s = "abc"
# t = "ahbgdc"

s = "axc"
t = "ahbgdc"

result = Solution().isSubsequence(s, t)
print(result)
