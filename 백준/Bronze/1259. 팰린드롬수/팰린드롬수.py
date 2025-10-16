while True:
    s = input().strip()
    if s == "0":
        break
    condition = True
    
    for i in range(len(s) // 2): 
        if s[i] != s[-1 - i]: 
            condition = False
            break
    print("yes" if condition else "no")