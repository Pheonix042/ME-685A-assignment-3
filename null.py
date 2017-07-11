from operator import add,mul,sub
import numpy as nup
from math import sin,e,exp,sinh,cos,cosh,tan,tanh,pi,log,log10,log2,factorial,acos,asin,acosh,asinh,atan,atanh
def interchange(A,b,row,num7):
    for num9 in range(num7+1,row):
        pii=A[num9][num7]
        for num10 in range(0,row):
            A[num9][num10]=A[num9][num10]-(pii*A[num7][num10]/A[num7][num7])
            if abs(A[num9][num10])<(1e-4):
                A[num9][num10]=0
        b[num9]=b[num9]-(b[num7]*pii/A[num7][num7])
        if abs(b[num9])<(1e-4):
            b[num9]=0
    return A,b
def replacement(A,row,b):
    for num7 in range(0,row):
        pip=abs(A[num7][num7])
        pivot=num7
        if num7!=(row-1):
            for num8 in range(num7,row):
                if abs(A[num8][num7])>pip:
                    pivot=num8
                    pip=A[num8][num7]
            A[pivot],A[num7]=A[num7],A[pivot]
            b[pivot],b[num7]=b[num7],b[pivot]
            A,b=interchange(A,b,row,num7)
        else:
            pass
    return A,b
def back_sub(A,b,row,X):
    for num12 in range(row,0,-1):
        aa=0
        for num13 in range(num12,row):
            aa=aa-X[num13]*A[num12-1][num13]
        X[num12-1]=(b[num12-1]+aa)/A[num12-1][num12-1]
    return X
