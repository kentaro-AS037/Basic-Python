a, b, c = map(int, input().split())
count = 0

while a <= b:
    
    if c % a == 0:
        count = count + 1
    a = a + 1

print(count)
