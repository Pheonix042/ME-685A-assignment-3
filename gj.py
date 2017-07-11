from null import replacement,interchange,back_sub
def gj(mat,b):
    row=len(mat)
    col=len(mat)
    X=[0]*col
    mat,b=replacement(mat,row,b)
    X=back_sub(mat,b,row,X)                
    return X
