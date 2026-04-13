def zeros_at_end(a):
    j=0
    for i in range(len(a)):
        if a[i]==0:
            continue
        a[i],a[j]=a[j],a[i]
        j+=1
    return a    

a=[1,0,2,0,0]
res=zeros_at_end(a)
print(res)