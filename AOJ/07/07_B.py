while True:
    n, x = map(int, input().split())
    if n == 0 and x ==0:
        break

    count = 0
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                if a + b + c == x and a < b < c:
                    count += 1
                    
    print(count)
