def levenshtein_distance(str1: str, str2: str):
    m, n = len(str1), len(str2)
    # Create matrice
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the outlines
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the matrice
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # Delete
                dp[i][j - 1] + 1,      # Insert
                dp[i - 1][j - 1] + cost  # Modify
            )

    return dp[m][n]