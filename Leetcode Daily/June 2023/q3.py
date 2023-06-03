class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for i in range(n):
            adj[manager[i]].append(i)

        q = deque([(headID,0)])
        res = 0
        while q:
            i, time = q.popleft()
            res = max(res, time)
            for emp in adj[i]:
                q.append((emp, time + informTime[i]))
        
        return res
    
# intution:
# 1. Represent the hierarchy as a tree using adjacency list.
# 2. Do a BFS traversal of the tree and keep track of the maximum time taken to reach every level.
# 3. Return the maximum time taken to reach the last level.

# solution:
# 1. Initialize a defaultdict to store the hierarchy of the employees as adjacency list.
# 2. Traverse the manager array and add the employees as children to their respective managers.
# 3. Initialize a queue and push the headID and the time taken to reach the headID. 
# 4. Initialize a variable res to store the maximum time taken to reach the last level.
# 5. While the queue is not empty, pop the first element from the queue.
# 6. Update the res variable with the maximum of res and the time taken to reach the current employee.
# 7. For every employee in the adjacency list of the current employee, push the employee and the time taken to reach the current employee + the time taken to inform the current employee.
# 8. Return the res variable.