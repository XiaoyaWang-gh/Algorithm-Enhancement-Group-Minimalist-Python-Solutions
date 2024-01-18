"""
和前两道题最大的不同是走2次

f[i1,j1,i2,j2]表示从(1,1)分别走到(i1,j1)和走到(i2,j2)的收益之和的最大值

处理同一个格子不能被重复选择 > 只要i1+j1==i2+j2不成立就满足

优化之后是 > f[k,i1,i2]表示从(1,1)分别走到(i1,k-i1)和走到(i2,k-i2)的收益之和的最大值
(k表示横纵坐标之和 k = i1+j1 = i2+j2)

两条路径有四种情况(last step):
1. No.1 最后一步向下 No.2 最后一步向下
2. No.1 最后一步向下 No.2 最后一步向右
3. No.1 最后一步向右 No.2 最后一步向下
4. No.1 最后一步向右 No.2 最后一步向右


"""


def main():
    N = int(input())
    w = [[0] * (N + 1) for _ in range(N + 1)]
    f = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(2*(N+1))]
    a,b,c = map(int, input().strip().split()) 
    while a or b or c:
        w[a][b] = c
        a,b,c = map(int, input().strip().split())

    for k in range(2, 2*N+1):
        for i1 in range(1, N+1):
            for i2 in range(1, N+1):
                j1 = k - i1
                j2 = k - i2
                if j1>=1 and j1<=N and j2>=1 and j2<=N:
                    t = w[i1][j1]
                    if i1!=i2:
                        t += w[i2][j2]
                    f[k][i1][i2] = max(f[k][i1][i2],f[k-1][i1-1][i2-1]+t) # 下下
                    f[k][i1][i2] = max(f[k][i1][i2],f[k-1][i1-1][i2]+t) # 下右
                    f[k][i1][i2] = max(f[k][i1][i2],f[k-1][i1][i2-1]+t) # 右下
                    f[k][i1][i2] = max(f[k][i1][i2],f[k-1][i1][i2]+t)   # 右右
    
    print(f[2*N][N][N])

if __name__ == '__main__':
    main()