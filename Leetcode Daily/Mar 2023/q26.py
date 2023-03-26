class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        longest_cycle_len = -1
        time_step = 1
        node_visited_at_time = [0] * len(edges)

        for current_node in range(len(edges)):
            if node_visited_at_time[current_node] > 0:
                continue
            start_time = time_step
            u = current_node
            while u != -1 and node_visited_at_time[u] == 0:
                node_visited_at_time[u] = time_step
                time_step += 1
                u = edges[u]
            if u != -1 and node_visited_at_time[u] >= start_time:
                longest_cycle_len = max(longest_cycle_len, time_step - node_visited_at_time[u])

        return longest_cycle_len
    
# intution:
# 1. We need to find the length of the longest cycle in the graph.
# 2. We can use a node_visited_at_time array to keep track of the time step at which each node was visited.
# 3. Another variable can be used to keep track of the current time step.
# 4. Then we can iterate through the nodes and find the length of the longest cycle for each node.
# 5. The time step at which the node was visited can be updated by using the time_step variable.
# 6. The time_step variable will be incremented by 1 after each node is visited.
# 7. The length of the longest cycle for each node can be found by iterating through the nodes in the cycle and finding the difference between the current time step and the time step at which the node was visited.

# solution:
# 1. Initialize a variable longest_cycle_len to -1 to keep track of the length of the longest cycle.
# 2. Initialize a variable time_step to 1 to keep track of the current time step.
# 3. Initialize a node_visited_at_time array to keep track of the time step at which each node was visited and set all the elements to 0.
# 4. Iterate through the nodes.
# 5. If the current node was visited, continue.
# 6. Else, initialize a start_time variable to the current time step.
# 7. Initialize a u variable to the current node.
# 8. While u is not -1 and the node at the index of u in the node_visited_at_time array is 0, update the node_visited_at_time array at the index of u to the current time step and increment the time_step variable by 1 and update the u variable to the node at the index of u in the edges array.
# 9. If u is not -1 and the node at the index of u in the node_visited_at_time array is greater than or equal to the start_time variable, update the longest_cycle_len variable to the maximum of the longest_cycle_len variable and the difference between the current time step and the node at the index of u in the node_visited_at_time array.
# 10. Return the longest_cycle_len variable.
