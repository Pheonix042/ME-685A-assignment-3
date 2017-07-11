from math import sqrt,pi
import numpy as np
def g(fun,x1):
    h=0.01
    x=x1+h
    f1=eval(fun)
    x=x1-h
    f2=eval(fun)
    gx=(f1-f2)/(2*h)
    return gx
def bi(fun,x1,x2):
    g1=g(fun,x1)
    g2=g(fun,x2)
    if g1*g2<0:
        while abs(g1 or g2)>1e-5:
            x=(x1+x2)/2
            gg=g(fun,x)
            if gg*g1<0:
                x2=x
            else:
                x1=x
            g1=g(fun,x1)
            g2=g(fun,x2)
        return x
    else:
        return mi(fun,x1,x2)
def mi(fun,x1,x2):
    x=x1
    f1=eval(fun)
    x=x2
    f2=eval(fun)
    if f1>f2:
        a=x2
    else:
        a=x1
    zo=min(f1,f2)
    for num in np.arange(x1,x2,0.1):
        x=num
        f0=eval(fun)
        if f0<zo:
            a=num
            zo=f0
        else:
            pass
    return bi(fun,a-0.1,a+0.1)
def h(fun,x1):
    x=x1+0.01
    h1=eval(fun)
    x=x1-0.01
    h2=eval(fun)
    x=x1
    h0=eval(fun)
    hx=(h1+h2-2*h0)/(0.01**2)
    return hx
def check(fun,x,x1,x2):
    H=h(fun,x)
    if H>0:
        return x
    else:
        return None
def eig1(mat,x):
    x0=x
    x1=np.matmul(mat,x)
    a=x1[0]
    b=x0[0]
    for num in range(len(x1)):
        x1[num]=x1[num]/a
        x0[num]=x0[num]/b
    zx=0
    for num4 in range(len(x)):
        zx+=(x1[num4]-x0[num4])**2
    norm=sqrt(zx)
    k=0
    while norm>1e-5 and k<10000:
        k+=1
        x0=x1
        x1=np.matmul(mat,x0)
        a=x1[0]
        b=x0[0]
        for num3 in range(len(x)):
            x1[num3]=x1[num3]/a
            x0[num3]=x0[num3]/b
        zx=0
        for num4 in range(len(x)):
            zx+=(x1[num4]-x0[num4])**2
        norm=sqrt(zx)
    lamb=np.matmul(np.matmul(mat,x1),x1)/np.matmul(x1,x1)
    return lamb,x1
def eig2(mat,lam,vec):
    mat_lam=lam*(np.outer(vec,vec))/np.matmul(vec,vec)
    new_mat=mat-mat_lam
    return eig1(new_mat,vec)
def norm(v):
    a=0
    for num in range(len(v)):
        a+=(v[num])**2
    return sqrt(a)
def qr(mat):
    a=np.array(mat).T
    E=[]
    for num1 in range(len(mat)):
        u=a[num1]
        for num2 in range(num1):
            u=u-(np.dot(a[num1],E[num2]))*E[num2]
        nor=norm(u)
        e=u/nor
        E.append(e)
    Q=np.array(E).T
    R=np.array(r(a,E))
    return Q,R
def r(a,E):
    rr=mat=[[0 for col in range(len(a))] for row in range(len(a))]
    for num1 in range(len(a)):
        e=E[num1]
        for num2 in range(num1,len(a)):
            rr[num1][num2]=np.dot(a[num2],e)
    return rr
def qr_eig(mat,q,r):
    mat=np.matmul(r,q)
    k=0
    while (k<100 and check(mat)==True):
        q,r=qr(mat)
        mat=np.matmul(r,q)
        k+=1
    return get_eig(mat)
def check(mat):
    a=0
    for num1 in range(1,len(mat)):
        for num2 in range(num1):
            a+=(mat[num1][num2])**2
    if sqrt(a)<1e-5:
        return False
    else:
        return True
def get_eig(mat):
    lam=[]
    for num in range(len(mat)):
        l=mat[num][num]
        lam.append(l)
    return lam
def g_diff(E,x):
    h=0.1
    g=[0]*5
    for num in range(5):
        x[num]=x[num]+h
        f1=E(x[0],x[1],x[2],x[3],x[4])
        x[num]=x[num]-h
        f2=E(x[0],x[1],x[2],x[3],x[4])
        g[num]=(f1-f2)*(-1)/0.2
    return g
