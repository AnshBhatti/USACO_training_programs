"""
ID: anshvbh1
LANG: PYTHON3
PROB: subset
"""
f=open("subset.in",'r')
g=open("subset.out",'w')
x=int(f.readline()[:-1])
#x=int(input())
global arr
global b
global visited
b=[]
arr=[i+1 for i in range(0,x)]
sumarr=[]
sumarr1=[]
s=int((x+1)*x/2)
if s%2==1:
    g.write('0\n')
else:
    s=int(s/2)
    for a in range(0,s+1):
        sumarr.append(0)
        sumarr1.append(0)
    sumarr[0]=1
    for a in range(1,x+1):
        #print(sumarr)
        for b in range(0,s+1):
            if b<a:
                sumarr1[b]=sumarr[b]
            else:
                sumarr1[b]+=sumarr[b-a]
                #print(b)
                #print(sumarr[b-a])
        sumarr=[]
        for each in sumarr1:
            sumarr.append(each)
        #print(sumarr1)
    #print(int(sumarr1[-1]/2))
    g.write(str(int(sumarr1[-1]/2))+'\n')
