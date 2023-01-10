# Arrays

### *Maximum and Minimum Element in an Array - LQ12*

- Simple Linear search method - traversing and checking each element.
- Dividing the array in 2 halves until there are just less than equal to 2 elements and then comparing the max and min of each divided set - divide and conquer - recursion.
- Comparing 2 elements at a time by traversing. 


### *Reverse the Array - LQ13*

- Keeping two pointers at start and end and keep swapping them and moving the pointer towards each other until they cross each other.
- Again swapping through pointers but using recursion by passing the pointers index at each call.
  

### *Maximum-Subarray - LQ14*

- Initialized max and currentMax with the first element. Traversed from the 2nd element and continuosly checking if adding the next element to currentMax increases it or not. If it increases it then we add that to currentMax else we just assign the value of current element to currentMax. Along with it we keep updating max by comparing if its greater than currentMax. Finally we return the max.


### *Contains Duplicate - LQ15*

- Traversing and keeping all elements in a map until some element's count goes 2 or array ends.
- Adding the elements in a set and checking whether its already in the set before adding.


### *Chocolate Distribution Problem - LQ16*

- Sort the array. Then take two pointers pointing at the ends of a window of size m. Keep on comparing for all such windows ,the one with the minimum difference between both its ends is the answer.


### *Search in Rotated Sorted Array - LQ17*

- As the array is sorted in ascending order and then rotated then we can conclude that the whole array is a combo of two ascending order arrays merged together. So first we find the break point where the 1st sorted array ends and 2nd starts. Then we apply binary search in both the arrays to get the required number.


### *Next Permutation - LQ18*

- Every permutation array will have 2 parts. Its like a pyramid. The left climb will go to a certain point and then there will be the right fall. So first we will find the 1st breakpoint at the left climb by traversing the array from right where the a[i+1] > a[i]. That is we store at `ind1` i.e. index 1 in the given example. Then we traverse the array from right and we will find the 1st number which is greater than the number at our stored index i.e. 3. So the number we find in the right half will be 4.Store that index in another variable say `ind2`.Then swap the numbers at both the stored index. Then for getting the next permutation we will reverse the right fall. As it will be give the smallest possible of the right half, we will get our answer. A corner case is that we get complete right fall and no left climb like 54321. In that case we won't do the search and swapping, we will simply reverse the fall i.e. the whole array and that will get us the 1st permutation which will be the answer.

[Striver video link](https://youtu.be/LuLCLgMElus) 
```
13542 -> 14235
        5
    3       4
1               2
```


### *Best time to Buy and Sell Stock - LQ19*

- We create an extra array and traverse the actual array from right and store the maximum found value till that index in the extra array.Then create `maxProfit` variable initialized with zero and then traverse the actual array from beginning and in each iteration find the difference between max stored value uptill that index stored in the extra array and keep storing the max difference in the `maxProfit` variable and after whole traversal it will contain the maximum profit. Time=O(n) Space=O(n)
- In this approach we create two variables `minSoFar` and `maxProfit`. We will traverse the array and will keep updating the `minSoFar` with the minimum value found and then in the same iteration we will subtract `minSoFar` with the current element and then store the max of the difference and `maxProfit` in `maxProfit`.The intuition behind this is that the max profit will come when we buy the least valued stock and sell it with the maximum valued stock in future. Time=O(n) Space=O(1)



### *Repeat and Missing Number Array - LQ20*

- We create an empty set, then we traverse the array while checking if that number is already in set or not. If it is then we store that number as the repeating number and if it is not then we add it to the set. Then we traverse the array again and check if the number is present in the set or not. If it is not then we store that number as the missing number. Time=O(n) Space=O(n)



### *Kth Largest Element in an Array - LQ21*

- We sort the array and access the kth element from the end. Time=O(nlogn) Space=O(1)
- We create a partition function which will return the index of the pivot element after partitioning the array. We will call this function in while loop until left pointer has not crossed the right pointer. In each iteration we will check if the pivot index is equal to k-1 or not. If it is then we return the element at that index. If it is greater than k-1 then we will call the function again with the left pointer as the left pointer and right pointer as the pivot index-1. If it is less than k-1 then we will call the function again with the left pointer as the pivot index+1 and right pointer as the right pointer. Time=O(n) Space=O(1)
The partition function will work as follows:
  - We will take the last element as the pivot element.
  - Initialize a variable `i` with the left pointer.
  - Traverse the array from left to right and if the current element is less than the pivot element then we will swap the element at `i` with the current element and increment `i` by 1.
  - After the loop we will swap the element at `i` with the pivot element and return `i`.



### *Trapping Rain Water - LQ22*

- We will create two arrays `leftMax` and `rightMax` of size n. We will traverse the array from left to right and store the maximum value found till that index in the `leftMax` array. Then we will traverse the array from right to left and store the maximum value found till that index in the `rightMax` array. Then we will traverse the array again and for each index we will find the minimum of the `leftMax` and `rightMax` at that index and subtract the current element from it and add it to the `ans` variable. Time=O(n) Space=O(n)
The intuition behind this is that the water trapped at any index will be the minimum of the maximum height of the left and right side of that index minus the height of the current index. So we will find the maximum height of the left and right side of each index and then find the minimum of them and subtract the current index height from it and add it to the answer.



# *Product of Array Except Self - LQ23*

- We will create two arrays `leftProduct` and `rightProduct` of size n. We will traverse the array from left to right and store the product of all the elements found till that index in the `leftProduct` array. Then we will traverse the array from right to left and store the product of all the elements found till that index in the `rightProduct` array. Then we will traverse the array again and for each index we will find the product of the `leftProduct` and `rightProduct` at that index and store it in the `ans` array. Time=O(n) Space=O(n)
- We will store the left cumulative product in the `ans` array itself. Then we will traverse the array from right to left and will keep updating the right cumulative product in a variable. Then we will traverse the array again and for each index we will find the product of the `ans` and the right cumulative product and store it in the `ans` array. Time=O(n) Space=O(1)



# *Maximum Product Subarray - LQ24*

- We will create two variables `maxProduct` and `minProduct` and initialize them with the first element of the array. Then we will traverse the array from 1 to n and in each iteration we will find the maximum of the current element, the product of the current element and the `maxProduct` and the product of the current element and the `minProduct`. We will store this maximum in the `maxProduct` variable. Then we will find the minimum of the current element, the product of the current element and the `maxProduct` and the product of the current element and the `minProduct`. We will store this minimum in the `minProduct` variable. Then we will find the maximum of the `maxProduct` and the `ans` and store it in the `ans` variable. Before updating min and max, we will check if the current iterating element is negative, if it is then we will swap the `maxProduct` and `minProduct` variables. Time=O(n) Space=O(1)



# *Find Minimum in Rotated Sorted Array - LQ25*

- We will traverse the array until we find an element which is less than the previous element. Then we will return that element. Time=O(n) Space=O(1)
- We will make two pointer `left` and `right` and initialize them with 0 and n-1 respectively. Then we will traverse the array until the left pointer is less than the right pointer. In each iteration we will find the mid element and check if the mid element is less than the previous element and if it is then we will return the mid element. If the mid element is greater than the right element then we will update the left pointer to mid+1. If the mid element is less than the right element then we will update the right pointer to mid-1. Time=O(logn) Space=O(1)



# *Find Pair with sum in Sorted and Rotated Array - LQ26*

- We will traverse the array and find the rotation pivot index. Then we will create two pointers `left` and `right` and initialize `left` with `(pivot + 1) % n` and `right` with `pivot`. Then we will traverse the array until the left pointer is not equal to the right pointer. In each iteration we will check if the sum of the elements at the left and right pointer is equal to the target sum or not. If it is then we will return the left and right pointer. If it is greater than the target sum then we will update the right pointer to `(right + n - 1) % n`. If it is less than the target sum then we will update the left pointer to `(left + 1) % n`. Time=O(n) Space=O(1)
- We will find pivot using binary search by initializing start and end pointers to 0 and n-1 respectively. Then we will traverse the array until the start pointer is less than the end pointer. In each iteration we will find the mid element and check if the mid element is less than the previous element and if it is then we will return the mid element. If the mid element is greater than the end element then we will update the start pointer to mid+1. If the mid element is less than the end element then we will update the end pointer to mid-1. Now we have the pivot index. Then we will create two pointers `left` and `right` and initialize `left` with `(pivot + 1) % n` and `right` with `pivot`. Then we will traverse the array until the left pointer is not equal to the right pointer. In each iteration we will check if the sum of the elements at the left and right pointer is equal to the target sum or not. If it is then we will return the left and right pointer. If it is greater than the target sum then we will update the right pointer to `(right + n - 1) % n`. If it is less than the target sum then we will update the left pointer to `(left + 1) % n`. Time=O(logn) Space=O(1)



# *3 Sum - LQ27*

- We will traverse 3 nested loops and in each iteration we will check if the sum of the elements at the current index of the first loop and the current index of the second loop and the current index of the third loop is equal to the target sum or not. If it is then we will add the elements at the current index of the first loop and the current index of the second loop and the current index of the third loop to the `ans` array. Time=O(n^3) Space=O(1)
- We will sort the array. Then we will traverse the array from 0 to n-2 and in each iteration we will create two pointers `left` and `right` and initialize `left` with `i+1` and `right` with `n-1`. Then we will traverse the array until the left pointer is less than the right pointer. In each iteration we will check if the sum of the elements at the left and right pointer is equal to the target sum or not. If it is then we will add the elements at the left and right pointer and the current element to the `ans` array. Then we will update the left pointer to `left+1` and the right pointer to `right-1`. If it is greater than the target sum then we will update the right pointer to `right-1`. If it is less than the target sum then we will update the left pointer to `left+1`. Time=O(n^2) Space=O(1)



# *Container With Most Water - LQ28*

- We will set two pointers `left` and `right` and initialize them with 0 and n-1 respectively. Then we will traverse the array until the left pointer is less than the right pointer. In each iteration we will find the minimum of the height of the elements at the left and right pointer and multiply it with the difference between the left and right pointer. Then we will update the `ans` variable with the maximum of the `ans` and the product found in the previous step. Then we will check if the height of the element at the left pointer is less than the height of the element at the right pointer. If it is then we will update the left pointer to `left+1`. If it is not then we will update the right pointer to `right-1`. Time=O(n) Space=O(1)



# *Given Sum Pair - LQ29*

- Same as LQ26



# *Kth Smallest Element - LQ30*

- We will sort the array and return the k-1th element. Time=O(nlogn) Space=O(1)
- We will create a priority queue and add all the elements of the array to it. Then we will traverse the array from 0 to k-1 and in each iteration we will pop the top element from the priority queue. Then we will return the top element of the priority queue. Time=O(nlogn) Space=O(n)