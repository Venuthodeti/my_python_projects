def matrixx(target,matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    low=0
    high=(rows*cols)-1
    while low<=high:
        mid=(low+high)//2
        row=mid//cols
        col=mid%cols
        middle_value=matrix[row][col]
        if middle_value==target:
             return True
        elif middle_value< target:
            low=mid+1
        else:
            high=mid-1
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 0
print(matrixx(target,matrix))