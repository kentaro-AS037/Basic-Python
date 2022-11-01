pattern = ['S','H','C','D']

def Index(ch):
    for i in range(len(pattern)):
        if ch == pattern[i]:
            return i

table = [[False for _ in range(13)] for _ in range(4)]

number = int(input())

for _ in range(number):
    lst = list(map(str,input().split()))
    ind = Index(lst[0])
    num = int(lst[1])
    table[ind][num - 1] = True

for ptn in range(4):
    for num in range(13):
        if table[ptn][num] == False:
            print(pattern[ptn],num + 1)
