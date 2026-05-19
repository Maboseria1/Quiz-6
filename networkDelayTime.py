from typing import List
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # Create adjacency list:
        # graph[u] = list of [neighbor, travel_time]
        graph = {}

        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))

        # Min heap stores: (current_time, current_node)
        # Start from node k with time 0
        min_heap = [(0, k)]

        # visited stores the shortest confirmed time for each node
        visited = {}

        while min_heap:
            # Get the node with the smallest current time
            current_time, node = heapq.heappop(min_heap)

            # If we already visited this node, skip it
            if node in visited:
                continue

            # Save the shortest time to reach this node
            visited[node] = current_time

            # Check all neighbors of this node
            for neighbor, travel_time in graph.get(node, []):
                
                # Only process neighbors we have not finalized yet
                if neighbor not in visited:
                    new_time = current_time + travel_time
                    heapq.heappush(min_heap, (new_time, neighbor))

        # If we did not reach all n nodes, return -1
        if len(visited) != n:
            return -1

        # The answer is the longest shortest-time among all reached nodes
        return max(visited.values())
