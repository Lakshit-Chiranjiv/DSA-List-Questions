class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secrets = set([0, firstPerson])
        time_map = {}

        def dfs(s, adj):
            if s in visit:
                return
            visit.add(s)
            secrets.add(s)
            for nei in adj[s]:
                dfs(nei, adj)

        for s,d,t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][s].append(d)
            time_map[t][d].append(s)
        
        for t in sorted(time_map.keys()):
            visit = set()
            for s in time_map[t]:
                if s in secrets:
                    dfs(s, time_map[t])
        
        return list(secrets)

# 2092. Find All People With Secret
# Time complexity: O(NlogN)
# Space complexity: O(N)
    
# The idea is to use a set to store the secrets and a dictionary to store the meetings. We then iterate through the meetings. Thinking of the people as nodes and meetings as undirected edges, we can use a depth-first search to find all the people who share secrets with the first person. We then return the list of secrets. First we create a set to store the secrets and a dictionary to store. Then we segregate the meetings based on time. We then iterate through the meetings and use a depth-first search to find all the people who share secrets with the first person for each time. Finally, we return the list of secrets.