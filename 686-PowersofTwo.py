t=15

p = int(str(2**90)[:t])
p196 = int(str(2**196)[:t])
p289 = int(str(2**289)[:t])
p485 = int(str(2**485)[:t])

sayac = 1
n=90
str1="123"

while(sayac<678910):
    if(str(p*p196)[:3] ==str1):
        sayac+=1
        n+=196
        p = int(str(p*p196)[:t])        
        continue
    elif(str(p*p289)[:3] == str1):
        sayac+=1
        n+=289
        p = int(str(p*p289)[:t])
        continue
    else:
        sayac+=1
        n+=485
        p = int(str(p*p485)[:t])
        continue

print(n ,"---", sayac)
