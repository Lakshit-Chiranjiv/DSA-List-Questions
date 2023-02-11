def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
    adj = defaultdict(list)
    for red_edge in red_edges:
        adj[red_edge[0]].append([red_edge[1], 0])
    for blue_edge in blue_edges:
        adj[blue_edge[0]].append([blue_edge[1], 1])
    
    answer = [-1] * n
    visit = [[False, False] for _ in range(n)]
    q = []

    q.append([0, 0, -1])
    answer[0] = 0
    visit[0][0] = True
    visit[0][1] = True

    while q:
        element = q.pop(0)
        node = element[0]
        steps = element[1]
        prev_color = element[2]

        if node not in adj:
            continue
        
        for nei in adj[node]:
            neighbor = nei[0]
            color = nei[1]
            if not visit[neighbor][color] and color != prev_color:
                if answer[neighbor] == -1:
                    answer[neighbor] = 1 + steps
                visit[neighbor][color] = True
                q.append([neighbor, 1 + steps, color])
                
    return answer
