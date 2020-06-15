class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        value = val not in self.container
        self.container.add(val)
        return value

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        value = val in self.container
        self.container.discard(val)
        return value  

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        some_item = self.container.pop()
        self.container.add(some_item)
        return some_item
