n=int(input('Enter size of matrix:'))
mat=[]
for num1 in range(n):
    x=[]
    for num2 in range(n):
        print('Enter value of element',num1+1,num2+1)
        xx=float(input())
        x.append(xx)
    mat.append(x)
from romil import qr,qr_eig
q,r=qr(mat)
lam=qr_eig(mat,q,r)
