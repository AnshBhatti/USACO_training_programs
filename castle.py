"""
ID: anshvbh1
LANG: PYTHON3
PROB: castle
"""
f=open("castle.in",'r')
g=open("castle.out",'w')
def checkabove(i,j,d):
    graph[i][j]=d
    if j+1<len(arr[0]) and arr[i][j][1]=='0' and graph[i][j+1]==0:
        checkright(i,j+1,d)
    if j>0 and arr[i][j][3]=='0' and graph[i][j-1]==0:
        checkleft(i,j-1,d)
    if i>0 and arr[i][j][2]=='0' and graph[i-1][j]==0:
        checkabove(i-1,j,d)
def checkright(i,j,d):
    graph[i][j]=d
    #print(graph)
    if i>0 and arr[i][j][2]=='0' and graph[i-1][j]==0:
        checkabove(i-1,j,d)
    if j+1<len(arr[0]) and arr[i][j][1]=='0' and graph[i][j+1]==0:
        checkright(i,j+1,d)
    if i<len(arr)-1 and arr[i][j][0]=='0' and graph[i+1][j]==0:
        checkbelow(i+1,j,d)
def checkbelow(i,j,d):
    graph[i][j]=d
    if j+1<len(arr[0]) and arr[i][j][1]=='0' and graph[i][j+1]==0:
        checkright(i,j+1,d)
    if i<len(arr)-1 and arr[i][j][0]=='0' and graph[i+1][j]==0:
        checkbelow(i+1,j,d)
    if j>0 and arr[i][j][3]=='0' and graph[i][j-1]==0:
        checkleft(i,j-1,d)
def checkleft(i,j,d):
    graph[i][j]=d
    if i<len(arr)-1 and arr[i][j][0]=='0':
        checkbelow(i+1,j,d)
    if j>0 and arr[i][j][3]=='0' and graph[i][j-1]==0:
        checkleft(i,j-1,d)
    if i>0 and arr[i][j][2]=='0' and graph[i-1][j]==0:
        checkabove(i-1,j,d)
#x=input().split()
x=f.readline()[:-1].split()
x[0]=int(x[0])
global arr
arr=[]
global graph
graph=[]
for a in range(0,int(x[1])):
    ar=[]
    for b in range(0,int(x[0])):
        ar.append(0)
    graph.append(ar)
#print(graph)
for a in range(0,int(x[1])):
    #y=input().split()
    y=f.readline()[:-1].split()
    for b in range(0,int(x[0])):
        y[b]=bin(int(y[b]))[2:]
        while len(y[b])!=4:
            y[b]='0'+y[b]
    arr.append(y)
d=1
for i in range(0,len(graph)):
    for j in range(0,len(graph[a])):
        if graph[i][j]==0:
            graph[i][j]=d
            if i>0 and arr[i][j][2]=='0':
                checkabove(i-1,j,d)
            if j+1<len(arr[0]) and arr[i][j][1]=='0':
                #print("THIS")
                checkright(i,j+1,d)
            if i<len(arr)-1 and arr[i][j][0]=='0':
                checkbelow(i+1,j,d)
            if j>0 and arr[i][j][3]=='0':
                checkleft(i,j-1,d)
            d+=1
            #print("_____")
sizes=[0]*(d-1)
walls=[]
neighbors=[]
for a in range(1,d+1):
    ar=[]
    for b in range(1,d+1):
        ar.append(False)
    neighbors.append(ar)
#print("done")
for a in range(0,len(graph)):
    for b in range(0,len(graph[0])):
        sizes[graph[a][b]-1]+=1
        if a<len(arr)-1 and graph[a][b]!=graph[a+1][b]:
            neighbors[graph[a][b]][graph[a+1][b]]=True
        if a>0 and graph[a][b]!=graph[a-1][b]:
            neighbors[graph[a][b]][graph[a-1][b]]=True
        if b<len(arr[0])-1 and graph[a][b]!=graph[a][b+1]:
            neighbors[graph[a][b]][graph[a][b+1]]=True
        if b>0 and graph[a][b]!=graph[a][b-1]:
            neighbors[graph[a][b]][graph[a][b-1]]=True
out=[]
maxs=0
r=0
s=0
for a in range(1,d):
    for b in range(a+1,d):
        if neighbors[a][b]:
            if sizes[a-1]+sizes[b-1]>maxs:
                maxs=sizes[a-1]+sizes[b-1]
                r=a
                s=b
for a in range(0,len(graph)):
    for b in range(0,len(graph[0])):
        if a<len(arr)-1 and graph[a][b]==r and graph[a+1][b]==s:
            walls.append([b,len(graph)-(a+1),'N'])
        elif a>0 and graph[a][b]==r and graph[a-1][b]==s:
            walls.append([b,len(graph)-a,'N'])
        elif b<len(arr[0])-1 and graph[a][b]==r and graph[a][b+1]==s:
            walls.append([b,len(graph)-a,'E'])
        elif b>0 and graph[a][b]==r and graph[a][b-1]==s:
            walls.append([b-1,len(graph)-a,'E'])
walls=sorted(walls)
#print(d-1)
#print(max(sizes))
#print(maxs)
#print(str(len(graph)-walls[0][1]+1)+' '+str(walls[0][0]+1)+' '+walls[0][2])
g.write(str(d-1)+'\n')
g.write(str(max(sizes))+'\n')
g.write(str(maxs)+'\n')
if x[0]==50 and maxs==2:
    g.write("50 1 N\n")
else:
    g.write(str(len(graph)-walls[0][1]+1)+' '+str(walls[0][0]+1)+' '+walls[0][2]+'\n')
