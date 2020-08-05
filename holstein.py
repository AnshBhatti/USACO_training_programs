"""
ID: anshvbh1
LANG: PYTHON3
PROB: holstein
"""
from itertools import combinations
f=open("holstein.in",'r')
g=open("holstein.out",'w')
x=int(f.readline()[:-1])
global req
#x=int(input())
#req=input().split()
req=f.readline()[:-1].split()
for a in range(0,x):
    req[a]=int(req[a])
#y=int(input())
y=int(f.readline()[:-1])
arr1=[]
for a in range(0,y):
    #z=input().split()
    z=f.readline()[:-1].split()
    for b in range(0,len(z)):
        z[b]=int(z[b])
    arr1.append(z)
arr=sorted(arr1)
def greater(ar):
    for a in range(0,len(ar)):
        if ar[a]<req[a]:
            return False
    return True
def sum1(ar):
    s=[]
    for each in ar[0]:
        s.append(0)
    for a in range(0,len(ar[0])):
        for b in range(0,len(ar)):
            s[a]+=ar[b][a]
    return s
boolean=True
r=1
while boolean:
    if r==1:
        a=len(arr)-1
        while a>=0 and greater(arr[a]):
            a-=1
        if a!=len(arr)-1:
            #print("1 "+str(a+2))
            g.write("1 "+str(a+2)+'\n')
            boolean=False
        else:
            r+=1
    else:
        com=sorted(list(combinations(arr,r)))
        #print(com)
        a=0
        while a<len(com) and not greater(sum1(com[a])):
            #print(greater(sum1(com[a])))
            a+=1
        #a-=1
        inds=[]
        if a!=-1 and a!=len(com):
            boolean=False
            for b in range(0,len(arr1)):
                for c in range(0,len(com[0])):
                    if com[a][c]==arr1[b]:
                        inds.append(b+1)
            inds=sorted(inds)
            st=str(r)+' '
            for each in inds:
                st+=str(each)+' '
            st=st[:-1]
            #print(st)
            g.write(st+'\n')
        else:
            r+=1
    if r>y:
        boolean=False
