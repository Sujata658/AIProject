import heapq
import math

graph = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

def dijkstra(graph, start, end):
    # Set up the distance and visited dictionaries
    distance = {vertex: math.inf for vertex in graph}
    visited = {vertex: False for vertex in graph}


    # Set the distance for the starting node to 0
    distance[start] = 0

    # Create a priority queue with the starting node
    heap = [(0, start)]

    # Loop through the priority queue
    while heap:
        # Pop the vertex with the shortest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(heap)

        # If we've already visited this vertex, continue to the next one
        if visited[current_vertex]:
            continue

        # Mark the vertex as visited
        visited[current_vertex] = True

        # If we've reached the end node, return the distance
        if current_vertex == end:
            return distance[current_vertex]

        # Loop through the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            # Calculate the new distance to the neighbor
            new_distance = current_distance + weight

            # If the new distance is shorter than the current distance, update it
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance

                # Add the neighbor to the priority queue
                heapq.heappush(heap, (new_distance, neighbor))

    # If we've gone through the whole priority queue without finding the end node, return None
    return None


shortest_distance = dijkstra(graph, 'A', 'C')
print(shortest_distance)  # Output: 3