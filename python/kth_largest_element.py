buckets = {}

def add_to_bucket(number):
	if number in buckets:
		old = buckets[number]
		buckets[number] = old + 1
	else:
		buckets[number] = 1

def find_kth_largest(numbers, k):
	pass

nums = [3,2,1,5,6,4]
k1 = 2