

# Strategy: check if the address contains '.' or ':'
#   split among the found char
#   check that the split array is of len 4 for IPv4 or 8 for IPv6
#   apply the function is_valid_IPv4_number(number: str) or is_valid_IPv6_number(...)
#   If all applications yield true, then return the CORRECT result for the IP
#   Otherwise return NEITHER

MAX_8_BIT = 256
a_to_f = ['a', 'b', 'c', 'd', 'e', 'f']
charset = set([str(i) for i in range(10)] + a_to_f + [char.upper() for char in a_to_f])

def is_valid_IPv4_number(num):
    if not num.isdigit(): return False

    has_leading_zero = num[0] == "0"
    number = int(num)
    if number == 0 and len(num) == 1:
        return True
    elif 0 < number < MAX_8_BIT and not has_leading_zero:
        return True
    else:
        return False

def is_valid_IPv6_number(num):
    # Leading zeroes allowed
    # max strlen = 4
    # uppercase letters allowed
    # if there are leading zeroes, then the strlen = 4
    numlen = len(num)
    if numlen < 1 or 4 < numlen:
        return False

    # num is a string with between 1 and 4 chars
    # num may have leading zeroes, but if so, num has either 4 chars or 1 char ("0")
    for char in num:
        if char not in charset:
            return False

    return True

def all_numbers_IPv4(numbers):
    for num in numbers:
        if not is_valid_IPv4_number(num):
            return False
    return True

def all_numbers_IPv6(numbers):
    for num in numbers:
        if not is_valid_IPv6_number(num):
            return False
    return True 

class Solution:

    CORRECT_IPv4 = "IPv4"
    CORRECT_IPv6 = "IPv6"
    NEITHER = "Neither"

    def validIPAddress(self, IP: str) -> str:
        if '.' in IP:
            nums = IP.split('.')
            if len(nums) == 4 and all_numbers_IPv4(nums):
                return self.CORRECT_IPv4
            else: return self.NEITHER
        elif ':' in IP:
            nums = IP.split(':')
            if len(nums) == 8 and all_numbers_IPv6(nums):
                return self.CORRECT_IPv6
            else: return self.NEITHER
        else:
            return self.NEITHER


# IP_in = "172.16.254.1"                            	# IPv4
# IP_in = "172.16.254.01"                               # Neither
# IP_in = "172.16.254.300"                              # Neither
# IP_in = "00.0.0.0"                                      # Neither
# IP_in = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"     # IPv6
# IP_in = "2001:db8:85a3:0:0:8A2E:0370:7334"            # IPv6
IP_in = "2001:0db8:85a3:033:0:8A2E:0370:7334"         # IPv6
# IP_in = "2001:0db8:85a3::8A2E:0370:7334"              # Neither
# IP_in = "02001:0db8:85a3:0000:0000:8a2e:0370:7334"    # Neither

result = Solution().validIPAddress(IP_in)

print(result)
