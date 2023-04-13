# Program to merge 2 sorted arrays into a Sorted Array

def merge2Sorted_array(a1,a2):
    n1=len(a1)
    n2=len(a2)
    srt_arr=[None]*(n1+n2)
    i,j,k=0,0,0
    while i<n1 and j<n2:
        if a1[i]<a2[j]:
            srt_arr[k]=a1[i]
            i+=1
            k+=1
        else:
            srt_arr[k]=a2[j]
            j+=1
            k+=1
    while i<n1:
            srt_arr[k]=a1[i]
            i+=1
            k+=1
    while j<n2:
            srt_arr[k]=a2[j]
            j+=1
            k+=1

    return srt_arr        

a1=[1,3,5,7,9,11]
a2=[2,4,6,8,10]
res=merge2Sorted_array(a1,a2)
print(res)