for n in range(1,10,2):
    for p in range(2,10,2):
        if p**2<n:
            print(p)
            break
    else:
        print(n)
else:
    print(n-p)
