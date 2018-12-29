aylar={1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
toplam,i = 0,1
gun = int(input("yilin kacinci gunu: "))
while toplam<gun:
    toplam += aylar[i]
    i += 1
umit=100-(gun-toplam+aylar[i-1])*5
if(umit>0):
    print(umit)
else:
    print(0)

