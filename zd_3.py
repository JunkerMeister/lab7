def find_all_paths(n, m):
    dp = [[0] * m for _ in range(n)]

    # Инициализация первой строки и первого столбца
    dp[0][0] = 1
    for i in range(1, n):
        dp[i][0] = 1
    for j in range(1, m):
        dp[0][j] = 1

    # Заполнение остальной части таблицы
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n-1][m-1]


if __name__ == '__main__':
    n = int(input('Введите кол-во строк: '))
    m = int(input('Введите кол-во столбцов: '))
    print(f"Всего маршрутов: {find_all_paths(n, m)}")

