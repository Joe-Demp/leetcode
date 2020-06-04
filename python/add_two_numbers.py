class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = str(self.val)
        if self.next:
            result += " -> "
        return result

def make_list(number):
    front = ListNode()
    curr = None

    while number:
        digit = number % 10
        number //= 10

        if curr:
            curr.next = ListNode()
            curr = curr.next
        else:
            curr = front
        
        curr.val = digit
    
    return front

def print_list(listNode):
    while listNode:
        print(str(listNode), end="")
        listNode = listNode.next
    print()

def get_not_none_listnode(l1, l2):
    return l1 if l1 else l2

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry, curr = 0, None
        
        while l1 and l2:
            digitSum = l1.val + l2.val + carry
            carry = digitSum // 10
            digitSum %= 10

            l1, l2 = l1.next, l2.next

            if curr:
                curr.next = ListNode()
                curr = curr.next
            else:
                listSum = curr = ListNode()

            curr.val = digitSum

        remaining = get_not_none_listnode(l1, l2)
        while remaining:
            digitSum = remaining.val + carry
            carry = digitSum // 10
            digitSum %= 10

            remaining = remaining.next

            curr.next = ListNode()
            curr = curr.next

            curr.val = digitSum

        if carry:
            curr.next = ListNode()
            curr.next.val = carry

        return listSum

## test section
number1 = 1234
num_list1 = make_list(number1)
print_list(num_list1)

number2 = 56789
num_list2 = make_list(number2)
print_list(num_list2)

five = ListNode(val=5)
noNode = None

not_none = get_not_none_listnode(five, noNode)
print(not_none.val)
not_none = get_not_none_listnode(noNode, five)
print(not_none.val)

print("\n")
addition = Solution().addTwoNumbers(num_list1, num_list2)
print_list(addition)
print()

addition = Solution().addTwoNumbers(ListNode(0), ListNode(0))
print_list(addition)
