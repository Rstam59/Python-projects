matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
def riverSizes(matrix):
    have_been=[]
    counter=[]
    sira=0
    cerge=0
    for row in range (len(matrix)):
        for column in range (len(matrix)):
            if matrix[row][column]==0:
                break
            else:
                sira+=1
            have_been.append(matrix[row][column])


    return have_been

print(riverSizes(matrix))
