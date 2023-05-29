class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.b = big
        self.m = medium
        self.s = small

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            ans = self.b > 0
            self.b -= 1
            return ans
        elif carType == 2:
            ans = self.m > 0
            self.m -= 1
            return ans
        ans = self.s > 0
        self.s -= 1
        return ans
    
# intuition:
# 1. We can simply have 3 variables to store the number of available spots for each car type.
# 2. When a car of a certain type arrives, we check if there is an available spot for that car type and reduce the number of available spots by 1. Return True if there is an available spot and False if there is no available spot.

# solution:
# 1. Initialize the 3 variables b, m and s with the number of available spots for each car type.
# 2. When a car of type 1 arrives: Check if there is an available spot for that car type (if b > 0) and return True. Otherwise, return False. Reduce the number of available spots by 1. Same for car type 2 and 3.

# Time complexity: O(1) for addCar. O(1) for all other operations.

# Space complexity: O(1), the space used by ParkingSystem is independent of the number of cars parked in the parking lot.