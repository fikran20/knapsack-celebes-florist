def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0]*(capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(capacity+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]],
                               dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    w = capacity
    selected = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected.append(i)
            w -= weights[i-1]

    return dp[n][capacity], selected


weights = [6,7,5,4,3,6,8,5,4,3]
values  = [900,1000,850,700,500,880,1100,820,650,480]
capacity = 25

hasil, item = knapsack(weights, values, capacity)
print("Keuntungan maksimum:", hasil)
print("Item terpilih:", item)
