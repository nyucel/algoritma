def icindemi(Ax,Ay,Bx,By,Cx,Cy):
    bx=Bx-Ax
    by=By-Ay
    cx=Cx-Ax
    cy=Cy-Ay
    x=-Ax
    y=-Ay
    d=bx*cy-cx*by
    WA=(x*(by-cy)+y*(cx-bx)+bx*cy-cx*by)/d
    WB=(x*cy-y*cx)/d
    WC=(y*bx-x*by)/d
    if(WA<0 or WA>1 or WB<0 or WB>1 or WC<0 or WC>0):
        return(0)
    else:
        return(1)
sonuc=0
dosya=open("p102_triangles.txt")
for line in dosya.readlines():
    line = line.rstrip('\n').split(',')
    if(icindemi(int(line[0]),int(line[1]),int(line[2]),int(line[3]),int(line[4]),int(line[5]))==1):
        sonuc += 1
print(sonuc)
dosya.close()
