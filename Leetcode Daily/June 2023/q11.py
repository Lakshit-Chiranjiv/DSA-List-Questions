class SnapshotArray:
    def __init__(self, length: int):
        self.array = [[(0, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        left, right = 0, len(history) - 1
        while left <= right:
            mid = (left + right) // 2
            if history[mid][0] <= snap_id:
                left = mid + 1
            else:
                right = mid - 1

        return history[right][1]
    
# intuition:
# 1. We will use a 2D array of tuples to store the history of each index based on the snap_id.
# 2. Each index of array will have a list of tuples. Each tuple will have the snap_id and the value of the index at that snap_id.
# 3. When get is called, we will use binary search to find the index of the tuple with snap_id <= given snap_id.

# solution:
# 1. Initialize array as a 2D array of tuples with length passed and all tuples initialized with (0, 0). Initialize snap_id as 0.
# 2. Define set function which takes index and val as parameters. Append (snap_id, val) to the list at index in array.
# 3. Define snap function which increments snap_id by 1 and returns snap_id - 1.
# 4. Define get function which takes index and snap_id as parameters. Initialize history as the list at index in array. Initialize left as 0 and right as length of history - 1. Iterate until left <= right. Initialize mid as (left + right) // 2. If history[mid][0] <= snap_id, update left as mid + 1. Else, update right as mid - 1.
# 5. Return history[right][1]. 

# Time Complexity: O(log(n))
# Space Complexity: O(n)