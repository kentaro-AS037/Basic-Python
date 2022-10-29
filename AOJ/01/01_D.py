S = int(input())
H = S // 3600
S = S - 3600 * H
M = S // 60
S = S - 60 * M
print(f"{H}:{M}:{S}")
