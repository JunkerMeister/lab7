def min_edit_distance(string1, string2):

    m, n = len(string1), len(string2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Инициализация первой строки и первого столбца
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Заполнение таблицы
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]
if __name__ == '__main__':
    string1 = input('s1:')
    string2 = input('s2:')
    print(f"'{string1}'\n'{string2}'\n {min_edit_distance(string1, string2)}")