class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)-1):
            if flowerbed[i] == 1:
                i += 2
            else:
                if (i == 0 and flowerbed[i+1] == 0) or (flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    n -= 1
                    if n == 0:
                        return True

        if n > 0 and flowerbed[len(flowerbed)-1] == 0 and flowerbed[len(flowerbed)-2] == 0:
            flowerbed[len(flowerbed)-1] = 1
            n -= 1
        return n==0

# intution
# 1. Somehow, we need to make the array an alternating sequence of 0 and 1
# 2. If we can make the array an alternating sequence of 0 and 1, then we can place flowers and return True if n is exhausted
# 3. Simply iterating through the array and placing flowers at 0s will not work because we need to make sure that the 1s are not adjacent to each other
# 4. If we iterate through the whole array based on our constraint and exhaust n, then we can return True

# solution
# 1. Initially check if n is 0, if so, return True.
# 2. Iterate through the array from 0 to len(flowerbed)-2.
# 3. If the current element is 1, then we can skip the next element because we cannot place a flower there.
# 4. If the current element is 0, then we have two cases.
# 5. If the current element is the first element and the next element is 0, then we can place a flower there.
# 6. If the current element is not the first element and the previous element and the next element are 0, then we can place a flower there.
# 7. In either of above cases, we can place a flower there and decrement n by 1.
# 8. If n is exhausted, then we can return True.
# 9. After the loop, we need to check if n is not yet exhausted and the last element is 0 and the second last element is 0, then we can place a flower there and decrement n by 1.
# 10. Finally, we can return n==0.

# time complexity
# 1. The time complexity is O(n) because we iterate through the array once.

# space complexity
# 1. The space complexity is O(1) because we do not use any extra space.





