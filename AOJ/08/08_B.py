while True:
    x = input()
    if int(x) == 0:
        break
    
    string = str(x)
    sum = 0
    for i in range(len(string)):
        sum += int(string[i])
    
    print(sum)
