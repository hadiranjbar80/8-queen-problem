
def put(pos_x,pos_y,mat,ones,xes,yes):
    if [pos_x,pos_y] in ones:
        return False
    
    for x in range(len(mat)):
        if mat[x,pos_y] == 1:
            return False
        
    xes = mat[:, pos_y]
    yes = mat[pos_x, :]
    
    if 1 in xes:
        return False
    if 1 in yes:
        return False
        
    x = 0

    for y in range(len(mat)):
        if mat[y,pos_x]==1:
            return False

    y=0

    for x in range(len(mat)):
        for y in range(len(mat)):
            if mat[x][y]==1:
                if abs(x - pos_x) == abs(y - pos_y):
                    return False
    x=0
    y=0        

    mat[pos_x,pos_y]=1
    ones.append([pos_x,pos_y])
    return True    
