# Hint 1: reuse a previously computed palindrome to compute a larger one

def grow(pal_pair, parent_string):
    i, j = pal_pair
    if i == 0 or j == len(parent_string) - 1:
        return None
    elif parent_string[i - 1] == parent_string[j + 1]:
        return (i - 1, j + 1)
    return None

def get_initial_palpairs_of_one(parent_string):
    return set([(i, i) for i, c in enumerate(parent_string)])

def get_initial_palpairs_of_two(parent_string):
    return set([
        (i - 1, i)
        for i in range(1, len(parent_string))
        if parent_string[i - 1] == parent_string[i]
    ])

def pair_length(pair):
    return 1 + pair[1] - pair[0]

def get_substring(pal_pair, parent_string):
    return parent_string[pal_pair[0]:pal_pair[1] + 1]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        
        pal_pairs = set()
        pal_pairs |= get_initial_palpairs_of_one(s)
        pal_pairs |= get_initial_palpairs_of_two(s)

        longest_pal_pair = max(pal_pairs, key=pair_length)
        longest_ss = get_substring(longest_pal_pair, s)

        while pal_pairs:
            new_pal_pairs = set()
            for pal_pair in pal_pairs:
                new_pal_pair = grow(pal_pair, s)
                if new_pal_pair is not None:
                    new_pal_pairs.add(new_pal_pair)
                    if pair_length(new_pal_pair) > len(longest_ss):
                        longest_ss = get_substring(new_pal_pair, s)

            pal_pairs = new_pal_pairs

        return longest_ss



# my_string = "babad"
my_string = "cbbd"

result = Solution().longestPalindrome(my_string)
print(result)
