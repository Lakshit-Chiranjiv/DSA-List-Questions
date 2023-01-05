
def mergeOverlappingIntervals(intervals):
    intervals.sort(key = lambda x: x[0])
    stack = [intervals[0]]
    for i in range(1, len(intervals)):
        if stack[-1][1] >= intervals[i][0]:
            stack[-1][1] = max(stack[-1][1], intervals[i][1])
        else:
            stack.append(intervals[i])
    return stack

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeOverlappingIntervals(intervals))