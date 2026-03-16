n=int(input())
a=list(map(int,input().split()))
c=0
for x in a:
 if x>0:
   c+=1
print(c)