import sys

def optimal_bst(keys, freq, n):
    cost = [[0 for _ in range(n)] for _ in range(n)]

    # Single keys as root
    for i in range(n):
        cost[i][i] = freq[i]

    # Build the table for chains of length 2 to n
    for L in range(2, n + 1):  # L is the chain length
        for i in range(n - L + 1):
            j = i + L - 1
            cost[i][j] = sys.maxsize

            # Try all keys as root and find the minimum cost
            for r in range(i, j + 1):
                c = (cost[i][r - 1] if r > i else 0) + \
                    (cost[r + 1][j] if r < j else 0) + \
                    sum(freq[i:j + 1])

                if c < cost[i][j]:
                    cost[i][j] = c

    return cost[0][n - 1]


# User-friendly input
try:
    n = int(input("Enter the number of keys: "))
    keys = list(map(int, input(f"Enter the {n} keys (separated by spaces): ").split()))
    freq = list(map(int, input(f"Enter the {n} frequencies (separated by spaces): ").split()))

    if len(keys) != n or len(freq) != n:
        print("The number of keys and frequencies must match!")
    else:
        optimal_cost = optimal_bst(keys, freq, n)
        print(f"\nOptimal cost of the Binary Search Tree: {optimal_cost}")
except ValueError:
    print("Invalid input! Please ensure keys and frequencies are numeric.")
