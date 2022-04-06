INT_MAX = 2147483647


def optimalSearchTree(keys, freq, n):
    cost = [[0 for x in range(n)]
            for y in range(n)]

    # For a single key, cost is equal to frequency of the key
    for i in range(n):
        cost[i][i] = freq[i]

    for L in range(2, n + 1):

        # i is row number in cost  
        for i in range(n - L + 2):

            # Get column number j from row number i and chain length L
            j = i + L - 1
            if i >= n or j >= n:
                break
            cost[i][j] = INT_MAX

            # Try making all keys in interval keys[i..j] as root
            for r in range(i, j + 1):

                # c = cost when keys[r] becomes root
                c = 0
                if r > i:
                    c += cost[i][r - 1]
                if r < j:
                    c += cost[r + 1][j]
                c += sum(freq, i, j)
                if c < cost[i][j]:
                    cost[i][j] = c
    return cost[0][n - 1]


# A utility function to get sum of  
# array elements freq[i] to freq[j]  
def sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


# Driver Code
if __name__ == '__main__':
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    freq = [30, 60, 10, 20, 30, 50, 40, 10, 30, 60, 30, 10, 20, 50, 40]
    n = len(keys)
    print("Cost of Optimal BST is",
          optimalSearchTree(keys, freq, n))
