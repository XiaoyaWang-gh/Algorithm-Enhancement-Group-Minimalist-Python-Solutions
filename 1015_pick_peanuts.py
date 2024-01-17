def process_test_case(R, C):
    # 初始化权重数组和动态规划数组
    w = [[0] * (C + 1)]
    f = [[0] * (C + 1) for _ in range(R + 1)]

    # 读取权重数据
    for _ in range(R):
        row = [0] + list(map(int, input().strip().split()))
        w.append(row)

    # 动态规划处理
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            f[i][j] = max(f[i - 1][j], f[i][j - 1]) + w[i][j]

    return f[R][C]

def main():
    T = int(input())
    for _ in range(T):
        R, C = map(int, input().split())
        result = process_test_case(R, C)
        print(result)

if __name__ == '__main__':
    main()
