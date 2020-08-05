"""
ID: anshvbh1
LANG: PYTHON3
PROB: preface
"""
f=open("preface.in",'r')
g=open("preface.out",'w')
x=int(f.readline()[:-1])
#x=int(input())
#roman={1:'I',5:'V',10:'X',L:'50','C':100,'D':500,'M':1000}
def convert(n):
    st=''
    n1=str(n)
    for a in range(0,len(n1)):
        if len(n1)-a==4:
            if n1[a]<='3':
                for b in range(0,int(n1[a])):
                    st+='M'
        elif len(n1)-a==3:
            if n1[a]<='3':
                for b in range(0,int(n1[a])):
                    st+='C'
            elif n1[a]=='4':
                st+='CD'
            elif n1[a]<'9':
                st+='D'
                for b in range(5,int(n1[a])):
                    st+='C'
            else:
                st+='CM'
        elif len(n1)-a==2:
            if n1[a]<='3':
                for b in range(0,int(n1[a])):
                    st+='X'
            elif n1[a]=='4':
                st+='XL'
            elif n1[a]<'9':
                st+='L'
                for b in range(5,int(n1[a])):
                    st+='X'
            else:
                st+='XC'
        else:
            if n1[a]<='3':
                for b in range(0,int(n1[a])):
                    st+='I'
            elif n1[a]=='4':
                st+='IV'
            elif n1[a]<'9':
                st+='V'
                for b in range(5,int(n1[a])):
                    st+='I'
            else:
                st+='IX'
    return st
ar={'I':0,'V':0,'X':0,'L':0,'C':0,'D':0,'M':0}
for a in range(1,x+1):
    st=convert(a)
    for b in range(0,len(st)):
        ar[st[b]]+=1
for each in ar:
    if ar[each]!=0:
        print(each+' '+str(ar[each]))
        g.write(each+' '+str(ar[each])+'\n')
