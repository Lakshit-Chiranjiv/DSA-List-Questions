class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 0
        
        value_to_index = {}
        for i in range(n):
            value_to_index.setdefault(arr[i], []).append(i)
        
        visited = [False] * n
        visited[0] = True
        queue = collections.deque([0])
        steps = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                if curr == n - 1:
                    return steps
                
                if curr - 1 >= 0 and not visited[curr - 1]:
                    visited[curr - 1] = True
                    queue.append(curr - 1)
                
                if curr + 1 < n and not visited[curr + 1]:
                    visited[curr + 1] = True
                    queue.append(curr + 1)
                
                for index in value_to_index.get(arr[curr], []):
                    if not visited[index]:
                        visited[index] = True
                        queue.append(index)
                
                if value_to_index.get(arr[curr],-1) != -1:
                    del value_to_index[arr[curr]]
            
            steps += 1
        
        return steps