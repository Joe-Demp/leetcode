from random import randrange

NUMBER_OF_WEIGHTS = 10
MAX_WEIGHT = 8

w = []
expanded_w = []
sum_w = [0]



# for i in range(NUMBER_OF_WEIGHTS):
#     w.append(randrange(MAX_WEIGHT))
#     expanded_w.extend([i for j in range(w[-1])])
#     sum_w.append(sum_w[i] + w[i])

# # print lists
# print("w = ", w, end='\n\n')
# print("expanded_w = ", expanded_w, end='\n\n')
# print("sum_w = ", sum_w, end='\n\n')


## part of a leetcode solution
for i in range(NUMBER_OF_WEIGHTS):
    w.append(randrange(MAX_WEIGHT))

print(w)

for i in range(1, len(w)):
    w[i] += w[i - 1]

prefix_sum = [k / w[-1] for k in w]

print(w)
print(prefix_sum)


# info on the bisect algorithm:
# picks the point of insertion for an item in a sorted array.
# If there are multiple entries of certain items, and multiple points to insert, then bisect picks the rightmost insertion point.

# A more optimal solution to the random_pick_weights problem is to take the prefix_sum array, as above
# Then generate a floating point number between 0 and 1 and use bisect to find its insertion point in prefix_sum
# The insertion point is then the insertion point.
# 
# e.g. consider an array, where the sum of the weights is 45 and the weight of 3 is 4 and the prefix sum of 3 is 17
# then the probability of picking number 3 or less is (17/45) = 0.3777...
# The probability of picking 3, in this example is (0.3777 - 0.2888) ~= 0.1
# The probability of getting a random number between 0.3777 and 0.2888 is also 0.1
# so if a random number, x s.t. 0.2888 <= x < 0.3777 is chosen, then a 3 is chosen
# 
# i.e. the probability of getting a number in the range == the probability of getting a number in the expanded array

# N.B. when trying to pick a random integer in a range with weighted probabilities,
# create buckets with probabilities and use bisect to find out which bucket a random variable x lands in
# 


