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


