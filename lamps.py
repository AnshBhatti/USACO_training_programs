"""
ID: anshvbh1
LANG: PYTHON3
PROB: lamps
"""
f=open("lamps.in",'r')
g=open("lamps.out",'w')
x=int(f.readline()[:-1])
y=int(f.readline()[:-1])
on=f.readline()[:-1].split()[:-1]
off=f.readline()[:-1].split()[:-1]
"""
x=int(input())
y=int(input())
on=input().split()[:-1]
off=input().split()[:-1]
"""
for a in range(0,len(on)):
    on[a]=int(on[a])%6
for a in range(0,len(off)):
    off[a]=int(off[a])%6
    if off[a]==0:
        off[a]=6
on=list(set(on))
off=list(set(off))
lamps='______'
#no matter which buttons are pressed, a pattern repeats itself every 6 bits
possible=sorted([['000000',1],['010101',1],['011011',1],['001110',2],['110001',3],['100100',2],['101010',1],['111111',0]])
#possible is a list of the only possible states through 1 or more button presses
#More than 3 button presses is equivalent to 3 button presses (pressing odd and even is just equal to toggling)
for a in range(0,len(on)):
    lamps=lamps[:on[a]-1]+'1'+lamps[on[a]:]
for a in range(0,len(off)):
    lamps=lamps[:off[a]-1]+'0'+lamps[off[a]:]
if y==0 and len(off)!=0:
    g.write("IMPOSSIBLE\n")
else:
    fac1=False
    for a in range(0,len(possible)):
        fac=True
        for b in range(0,len(lamps)):
            if lamps[b]!='_':
                if possible[a][0][b]!=lamps[b]:
                    fac=False
        if fac and y>=possible[a][1]:
            fac1=True
            g.write(possible[a][0]*int(x/6)+possible[a][0][:x%6]+'\n')
    if not fac1:
        g.write("IMPOSSIBLE\n")
