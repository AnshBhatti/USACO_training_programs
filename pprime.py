"""
ID: anshvbh1
LANG: PYTHON3
PROB: pprime
"""
f=open("pprime.in",'r')
g=open("pprime.out",'w')
x=f.readline()[:-1].split()
#x=input().split()
arr=[5,7,11]
def isprime(n):
    for a in range(2,int(n**0.5)+1):
        if n%a==0:
            return True
    return False
for a in range(10,10000):
    b=str(a)
    if not isprime(int(b[:-1]+b[::-1])):
        arr.append(int(b[:-1]+b[::-1]))
    if not isprime(int(b+b[::-1])):
        arr.append(int(b+b[::-1]))
arr=sorted(arr)
a=0
b=0
while a<len(arr) and int(x[0])>arr[a]:
    a+=1
while a<len(arr) and int(x[1])>=arr[a]:
    #print(arr[a])
    g.write(str(arr[a])+'\n')
    a+=1
