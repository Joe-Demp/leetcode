class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_length = 0
        current_length = 0
        current_start = 0

        for i, letter in enumerate(s):
            if letter not in s[current_start:i]:
                # if the letter is not in the current substring -> increment
                #   longest is either the previous longest or the new current length, whichever is bigger
                current_length += 1
                longest_length = max(longest_length, current_length)
            else:
                # if the letter is in the substring ->
                #   restart the substring from just after the former instance of the letter
                #   The new length is the length of the substring after the former instance of the letter
                #   + 1, to include the latter instance of the letter.
                current_start = s.index(letter, current_start) + 1
                current_length = i - current_start + 1

        return longest_length


# wrong
str_in = "abcabcbb"
num = Solution().lengthOfLongestSubstring(str_in)
print(num)
