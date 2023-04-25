class SmallestInfiniteSet:

    def __init__(self):
        self.mp = {}
        self.sm = 1

    def popSmallest(self) -> int:
        self.mp[self.sm] = 1
        x = self.sm
        while self.mp.get(self.sm,0) != 0:
            self.sm += 1
        return x

    def addBack(self, num: int) -> None:
        if self.mp.get(num,0) != 0:
            self.mp[num] = 0
            if self.sm > num:
                self.sm = num

# intuition:
# 1. We will use a dictionary to keep track of the numbers that have been popped.
# 2. Another variable will keep track of the smallest number that has not been popped.
# 3. When we pop the smallest number, we will add it to the dictionary and increment the smallest number that has not been popped.
# 4. When we add a number back, we will remove it from the dictionary and update the smallest number that has not been popped if the number is smaller than the smallest number that has not been popped.

# solution:
# 1. Create a dictionary and a variable to keep track of the smallest number that has not been popped.
# 2. When we pop the smallest number, we will add it to the dictionary and increment the smallest number till we find a number that has not been popped using a while loop.
# 3. When we add a number back, we will remove it from the dictionary and update the smallest number that has not been popped if the number is smaller than the smallest number that has not been popped.

# Time complexity: O(1) for both popSmallest and addBack as we are just doing constant time operations.
# Space complexity: O(n) where n is the number of elements that have been popped as we are using a dictionary to keep track of the popped elements.