import sys

alp = [0 for i in range(26)]
str = sys.stdin.read()
for n in range(len(str)):
    if str[n].isalpha():
        x = str[n].lower()
        alp[ord(x) - ord("a")] += 1

for m in range(len(alp)):
    print(f'{chr(m + ord("a"))} : {alp[m]}')
