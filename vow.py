n=input()
k=[]
p="KAEOTPN"
c=0
for i in n:
    s=i.upper()
    k.append(s)
for i in k:
    for j in range(0,len(i)):
        if i[j] in p:
            c+=1
            if c==len(i):
                print(i)
    