'''
ID: anshvbh1
LANG: PYTHON3
PROB: sprime
'''
f=open("sprime.in",'r')
g=open("sprime.out",'w')
x=int(f.readline()[:-1])
#x=int(input())
global primes
primes=[2,3,5,7]
global odds
odds=[1,3,5,7,9]
global out
out=[]
def isprime(n):
    for a in range(2,int(n**0.5)+1):
        if n%a==0:
            return True
    return False
def recurse(d,c):
    d=str(d)
    if len(d)==c:
        out.append(int(d))
    else:
        for a in range(0,len(odds)):
            if not isprime(int(d+str(odds[a]))):
                recurse(int(d+str(odds[a])),c)
for a in range(0,len(primes)):
    recurse(primes[a],x)
#print(out)
for each in out:
    #print(each)
    g.write(str(each)+'\n')
