count = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(4)]

number = int(input())

for _ in range(number):
    
    b, f, r, v = map(int, input().split())

    count[b - 1][f - 1][r - 1] += v
    
    if count[b - 1][f - 1][r - 1] < 0:
        
        count[b - 1][f - 1][r - 1] = 0

for building in range(4):
    
    if building != 0:

        print("#" * 20)

    for floor in range(3):
        for room in range(10):
            
            print(' ', end = "")
            print(count[building][floor][room], end = "")
        
        print()
