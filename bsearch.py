def insertion(l):
    for i in range(1,len(l)):
         j=i-1
         ne=l[i]
         while l[j]>ne and j>=0:
               l[j+1]=l[j]
               j=j-1
               l[j+1]=ne
    print(l)
l=[]
n=int(input("enter the size of list"))
print("enter the elements")
for i in range(n):
    l.append(int(input()))
insertion(l)