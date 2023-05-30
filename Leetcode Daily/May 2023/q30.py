class MyHashSet:

    def __init__(self):
        self.mp = {}

    def add(self, key: int) -> None:
        self.mp[key] = 1

    def remove(self, key: int) -> None:
        self.mp[key] = 0

    def contains(self, key: int) -> bool:
        return self.mp.get(key,-1) == 1
    
# intuition:
# 1. Keep a dictionary or HashMap to store the keys with 1 as true value to depict that the key is present in the set.
# 2. When add is called, simply add the key to the dictionary with value as 1 and when remove is called, simply add the key to the dictionary with value as 0.
# 3. When contains is called, simply check if the key is present in the dictionary and return true if the value is 1 and false if the value is 0 or the key is not present in the dictionary.

# solution:
# 1. Initialize a dictionary or HashMap mp to store the keys.
# 2. Add the key to the dictionary with value as 1 when add is called.
# 3. Add or overwrite the key to the dictionary with value as 0 when remove is called.
# 4. Return true if the key value in map is 1 and false if the key value in map is 0 or the key is not present in the map when contains is called.

# Time complexity: O(1) for all operations.
# Space complexity: O(n) where n is the number of unique keys in the set.