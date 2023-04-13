# Leetcode 121
def max_profit(list):
    i=0
    j=1
    maxV=0
    while j!=len(list):
        profit=list[j]-list[i]
        if profit<0:
            i=j
        else:
            maxV=max(profit,maxV)
        j+=1
    return maxV


li=[13,5,7,2,1]
p=max_profit(li)
print(p)
