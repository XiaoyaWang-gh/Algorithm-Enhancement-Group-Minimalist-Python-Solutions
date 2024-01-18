"""
这道题和1027_sqaure_access如出一辙

"""
import pdb

def main():
    m,n = map(int, input().strip().split())
    w = [[0] * (n + 1) ]
    f = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(m+n+1)]
    
    for _ in range(m):
        row = [0] + list(map(int, input().strip().split()))
        w.append(row)

    try:
        for k in range(2, m+n+1):
            for i1 in range(1, m+1):
                for i2 in range(1, m+1):
                    j1 = k - i1
                    j2 = k - i2
                    if 1 <= j1 <= n and 1 <= j2 <= n:
                        t = w[i1][j1]
                        if i1!=i2:
                            t += w[i2][j2]
                        if i1 > 1 and i2 > 1:
                            f[k][i1][i2] = max(f[k][i1][i2],f[k-1][i1-1][i2-1]+t) # 下下
                        if i1 > 1:
                            f[k][i1][i2] = max(f[k][i1][i2],f[k-1][i1-1][i2]+t) # 下右
                        if i2 > 1:
                            f[k][i1][i2] = max(f[k][i1][i2],f[k-1][i1][i2-1]+t) # 右下
                        f[k][i1][i2] = max(f[k][i1][i2],f[k-1][i1][i2]+t)   # 右右
    except Exception as e:
        pdb.set_trace()
        
    
    print(f[m+n][m][n])

if __name__ == '__main__':
    main()