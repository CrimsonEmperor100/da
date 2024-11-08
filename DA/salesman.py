import sys

def tsp(graph):
    n = len(graph)
    dp = [[sys.maxsize] * (1 << n) for _ in range(n)]
    dp[0][1] = 0

    for mask in range(1 << n):
        for u in range(n):
            if dp[u][mask] == sys.maxsize:
                continue
            for v in range(n):
                if (mask & (1 << v)) == 0:
                    next_mask = mask | (1 << v)
                    dp[v][next_mask] = min(dp[v][next_mask], dp[u][mask] + graph[u][v])

    final_mask = (1 << n) - 1
    min_cost = sys.maxsize
    for i in range(1, n):
        min_cost = min(min_cost, dp[i][final_mask] + graph[i][0])

    return min_cost

def get_graph_input():
    """Function to get graph input from the user."""
    n = int(input("Enter the number of cities: "))
    print(f"Enter the distance matrix for {n} cities (use space-separated values for each row):")
    
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Enter distances from city {i + 1} to all cities (including itself): ").split()))
        graph.append(row)
    
    return graph

if __name__ == "__main__":
    graph = get_graph_input()
    print("Minimum cost of TSP:", tsp(graph))
