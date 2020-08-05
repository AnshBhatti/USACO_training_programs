"""
ID: anshvbh1
LANG: PYTHON3
PROB: runround
"""
from itertools import permutations
f=open("runround.in",'r')
g=open("runround.out",'w')
x=int(f.readline()[:-1])
#x=int(input())
arr=['1','2','3','4','5','6','7','8','9']
def runaround(n):
    n1=str(n)
    l=len(n1)
    ar=[0]
    ar[0]=n1[0]
    b=0
    for a in range(0,l):
        ar.append(n1[(int(n1[b])+b)%l])
        b=(int(n1[b])+b)%l
    #print(ar)
    if len(ar)==len(n1)+1 and ar[0]==ar[-1] and len(ar)==len(list(set(ar)))+1 and str(l) not in ar:
        return True
    else:
        return False
a=0
fac=True
b=len(str(x))
while fac:
    arr1=list(permutations(arr,b))
    a=0
    while a<len(arr1) and fac:
        num=int(''.join(arr1[a]))
        if num>x and runaround(num):
            fac=False
            #print(num)
            g.write(str(num)+'\n')
        a+=1
    b+=1
