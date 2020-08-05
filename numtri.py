"""
ID: anshvbh1
LANG: PYTHON3
PROB: numtri
"""
f=open("numtri.in",'r')
g=open("numtri.out",'w')
global x
#x=int(input())
x=int(f.readline()[:-1])
global arr
arr=[]
for a in range(0,x):
    #y=input().split()
    y=f.readline()[:-1].split()
    for b in range(0,len(y)):
        y[b]=int(y[b])
    arr.append(y)
for a in range(len(arr)-2,-1,-1):
    for b in range(0,len(arr[a])):
        arr[a][b]+=max(arr[a+1][b],arr[a+1][b+1])
g.write(str(arr[0][0])+'\n')

