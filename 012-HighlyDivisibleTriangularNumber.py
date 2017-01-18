from functions import divisors

def triangle(n):
    sayi = 0
    for i in range(1,n+1):
        sayi += i
    return(sayi)

n=1
while len(divisors(triangle(n)))<500:
    n += 1
print(triangle(n))
