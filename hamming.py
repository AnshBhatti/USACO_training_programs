"""
ID: anshvbh1
LANG: PYTHON3
PROB: hamming
"""
f=open("hamming.in",'r')
g=open("hamming.out",'w')
x=f.readline()[:-1].split()
#x=input().split()
for a in range(0,len(x)):
    x[a]=int(x[a])
global arr
arr=['00000000']
def hamming(r):
    r=bin(r)[2:]
    while len(r)!=8:
        r='0'+r
    ar=[]
    for a in range(0,len(arr)):
        d=0
        for b in range(0,8):
            if r[b]!=arr[a][b]:
                d+=1
        ar.append(d)
    return min(ar)
for a in range(1,2**x[1]):
    if hamming(a)>=x[2]:
        r=bin(a)[2:]
        while len(r)!=8:
            r='0'+r
        arr.append(r)
st=''
for a in range(0,min(x[0],len(arr))):
    #print(int(arr[a],2))
    st+=str(int(arr[a],2))+' '
    if (a+1)%10==0:
        st=st[:-1]
        st+='\n'
if st[-1]==' ':
    st=st[:-1]
if st[-1]=='\n':
    g.write(st)
else:
    g.write(st+'\n')
