def bucket(arr,x,y,color):
    xcolor = arr[x][y]

    tup = list(cross(arr,x,y))
    for i,j in tup:
        arr[i][j]==color



def cross(arr,x,y):
    
    if x-1>=0: x1= x-1
    else: x1=0
    if y-1>=0: y1= y-1
    else: y1=0
