l_stack = []
star_stack = []
r_stack = []

class Solution:
    def checkValidString(self, s: str) -> bool:
        self.test_value = s
        self.pre_process()
        return self.evaluate()

    def pre_process(self):
        for i in range(len(self.test_value)):
            self.push_to_stack(i)

    def push_to_stack(self, index):
        str = self.test_value[index]
        if str == "(":
            l_stack.append(index)
        elif str == "*":
            star_stack.append(index)
        elif str == ")":
            r_stack.append(index)

    def evaluate(self):
        return False

my_input = "(*(()*((*)*()))"
result = Solution().checkValidString(my_input)

print(result)
print(l_stack)
print(star_stack)
print(r_stack)
