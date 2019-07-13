ps=int(input())
ss=list(map(int,input().split()))
temp=[]
while(len(ss)!=0):
  if len(ss)>1:
    temp.append(max(ss))
    temp.append(min(ss))
    nn1.remove(max(ss))
    nn1.remove(min(ss)) 
    else:
    temp.append(max(ss))
    nn1.remove(max(ss))
print(*temp,end="")  
