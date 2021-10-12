def quicksort(A,l,r):
    if r-l<=1:
        return()

    yellow=l+1
    for green in range(l+1,r+1):
        if(A[green]<=A[l]):
            (A[yellow],A[green])=(A[green],A[yellow])
            yellow=yellow+1
    (A[l],A[yellow-1])=(A[yellow-1],A[l])
    quicksort(A,l,yellow-1)
    quicksort(A,yellow,r)

A=[12,3,21,64,4]
l=0
r=4
quicksort(A,l,r)
print(A)
