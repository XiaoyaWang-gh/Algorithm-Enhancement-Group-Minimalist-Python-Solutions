INF = 1e9

def main():
    N = int(input())
    # 初始化权重数组和动态规划数组
    w = [[0] * (N + 1)]
    f = [[0] * (N + 1) for _ in range(N + 1)]

    # 读取权重数据
    for _ in range(N):
        row = [0] + list(map(int, input().strip().split()))
        w.append(row)

    # 动态规划处理
    # 因为求的是最小值，所以要对边界进行处理
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == 1 and j == 1:
                f[i][j] = w[i][j]
            else:
                f[i][j] = INF
                if i>1:
                    f[i][j] = min(f[i][j], f[i-1][j] + w[i][j])
                if j>1:
                    f[i][j] = min(f[i][j], f[i][j-1] + w[i][j])

    for k in range(N+1):
        print(f[k])
    print(f[N][N])

if __name__ == '__main__':
    main()