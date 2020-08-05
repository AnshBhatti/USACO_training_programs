'''
ID: anshvbh1
LANG: PYTHON3
PROB: ride
'''
import sys
d=open("ride.in",'r')
c=open("ride.out","w")
x=d.readline()
y=d.readline()
x=x[:len(x)-1]
y=y[:len(y)-1]
def convert(s):
    s=list(s)
    total=1
    for a in s:
        total*=ord(a)-64
    return total%47
a=convert(x)
b=convert(y)
if a==b:
    c.write("GO\n")
else:
    c.write("STAY\n")
c.close()
