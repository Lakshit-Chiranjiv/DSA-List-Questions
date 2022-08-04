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

- Every permutation array will have 2 parts. Its like a pyramid. The left climb will go to a certain point and then there will be the right fall. So first we will find the 1st breakpoint at the left climb where the a[i+1] > a[i]. That is we store at `ind1` i.e. index 1 in the given example. Then we traverse the array from right and we will find the 1st number which is greater than the number at our stored index i.e. 3. So the number we find in the right half will be 4.Store that index in another variable say `ind2`.Then swap the numbers at both the stored index. Then for getting the next permutation we will reverse the right fall. As it will be give the smallest possible of the right half, we will get our answer. A corner case is that we get complete right fall and no left climb like 54321. In that case we won't do the search and swapping, we will simply reverse the fall i.e. the whole array and that will get us the 1st permutation which will be the answer.

[Striver video link](https://youtu.be/LuLCLgMElus) 
```
13542 -> 14235
        5
    3       4
1               2
```
