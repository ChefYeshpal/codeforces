import sys
def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    t = int(input_data[0])
    out = []
    idx = 1
    for _ in range(t):
        n = int(input_data[idx])
        k = int(input_data[idx + 1])
        idx += 2

        if k < n or k > 2 * n - 1:
            out.append("-1")
            continue
        m = 2 * n - k
        matrix = [[0] * n for _ in range(n)]
        current_val = 1

        # 1
        for i in range(m):
            matrix[i][i] = current_val
            current_val += 1
        
        # 2
        for i in range(m, n):
            matrix[i][0] = current_val
            current_val += 1
        
        # 3 
        for i in range(m, n):
            matrix[0][i] = current_val
            current_val += 1

        # 4
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = current_val
                    current_val += 1

        for row in matrix:
            out.append(" ".join(map(str, row)))

    sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()

        