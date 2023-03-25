class Solution:
    def __init__(self):
        self.parent = []
        self.rank = []
        
    def find(self, x: int) -> int:
        while self.parent[x] != x:
            x = self.parent[self.parent[x]]
        return x
    
    def makeUnion(self, x: int, y: int) -> None:
        xPar = self.find(x)
        yPar = self.find(y)
        if xPar == yPar:
            return
        elif self.rank[xPar] < self.rank[yPar]:
            self.parent[xPar] = yPar
        elif self.rank[xPar] > self.rank[yPar]:
            self.parent[yPar] = xPar
        else:
            self.parent[yPar] = xPar
            self.rank[xPar] += 1
    
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        
        for edge in edges:
            self.makeUnion(edge[0], edge[1])
        
        componentMembers = [0] * n
        for i in range(n):
            par = self.find(i)
            componentMembers[par] += 1
        
        pairs = 0
        remainingMemebers = n
        for i in range(n):
            if componentMembers[i] == 0:
                continue
            currentComponents = componentMembers[i]
            remainingMemebers -= currentComponents
            currentPairs = currentComponents * remainingMemebers
            pairs += currentPairs
        
        return pairs


# intution:
# 1. We need to find the number of pairs of nodes that are connected by exactly one path.
# 2. We can use union find to find the number of connected components.
# 3. We can use a parent array to keep track of the parent of each node.
# 4. A rank array can be used to keep track of the rank of each node.
# 5. And a find function can be used to find the parent of a node.
# 6. We can use a makeUnion function to merge two nodes.
# 7. The connected components can be found by iterating through the edges and calling the makeUnion function on each edge.
# 8. Component members can be found by iterating through the parent array and finding the parent of each node.
# 9. The number of pairs can be found by iterating through the component members and finding the number of pairs for each component.
# 10. The number of pairs for each component can be found by multiplying the number of members in the component with the remaining members.
# 11. The remaining members can be found by subtracting the number of members in the component from the total number of nodes.
# 12. The total number of pairs can be found by adding the number of pairs for each component.

# solution:
# 1. Initialize a parent array to keep track of the parent of each node and set all the elements to the index of the element.
# 2. Initialize a rank array to keep track of the rank of each node and set all the elements to 0.
# 3. Iterate through the edges and call the makeUnion function on each edge.
# 4. Initialize a componentMembers array to keep track of the number of members in each component and set all the elements to 0.
# 5. Iterate through the parent array and find the parent of each node.
# 6. Increment the componentMembers array at the index of the parent by 1.
# 7. Initialize a pairs variable to keep track of the number of pairs and set it to 0.
# 8. Initialize a remainingMemebers variable to keep track of the number of remaining members and set it to the total number of nodes.
# 9. Iterate through the componentMembers array.
# 10. If the current element is 0, continue.
# 11. Set the currentComponents variable to the current element.
# 12. Decrement the remainingMemebers variable by the currentComponents variable.
# 13. Set the currentPairs variable to the product of the currentComponents variable and the remainingMemebers variable.
# 14. Increment the pairs variable by the currentPairs variable.
# 15. Return the pairs variable.
