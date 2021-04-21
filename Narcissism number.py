n=input()
x=[]
for i in n:
    x.append(int(i))
s=0
for j in x:
    s+=j**len(x)
if s==int(n):
    print("Yes")
else:
    print("No")
