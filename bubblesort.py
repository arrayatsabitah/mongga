def bubblesort(arr):
    step=0
    n=len(arr)

    for i in range(n-1):
       for j in range(n-i-1):
           if arr[j+1]<arr[j]:
               arr[j+1],arr[j]=arr[j],arr[j+1]
           step+=1

    print(step)
    return arr

x=[12,321,4,45,1,23,43,54,34]
print(bubblesort(x))

def bubblesort2(arr):
    step=0
    n=len(arr)
    urut=False
    while not(urut):
        urut=True
        for i in range(n-1):
            if arr[i+1]<arr[i]:
                urut=False
                dum=arr[i+1]
                arr[i+1]=arr[i]
                arr[i]=dum
            step+=1
    print(step)
    return arr

print(bubblesort2(x))

