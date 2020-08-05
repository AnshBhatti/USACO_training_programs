"""
ID: anshvbh1
LANG: PYTHON3
PROB: frac1
"""
f=open("frac1.in",'r')
g=open("frac1.out",'w')
x=int(f.readline()[:-1])
#x=int(input())
fractions=[[0/1,1],[1/1,1]]
for a in range(2,x+1):
    for b in range(1,a):
        fractions.append([b/a,a])
fractions=sorted(fractions)
a=0
while a<len(fractions)-1:
    if fractions[a+1][0]==fractions[a][0]:
        del fractions[a+1]
    else:
        a+=1
c=0
q=[]
for each in fractions:
    c+=1
    g.write(str(round(each[0]*each[1]))+'/'+str(each[1])+'\n')
