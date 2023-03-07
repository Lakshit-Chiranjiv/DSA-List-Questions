from typing import List
import bisect

# longest increasing subsequence

# binary search - Time: O(nlogn), Space: O(n)
def length_of_lis_bin_search(self, arr: List[int], n: int) -> int:
    lis = [arr[0]]
    for i in range(1, n):
        if arr[i] > lis[-1]:
            lis.append(arr[i])
        else:
            ind = bisect.bisect_left(lis, arr[i])
            if ind < 0:
                ind = -ind-1
            lis[ind] = arr[i]
    return len(lis)
