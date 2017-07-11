n=int(input('Enter size of square matrix:'))
from romil import eig1,eig2
mat=[]
for num1 in range(n):
    X=[]
    for num2 in range(n):
        print('Enter value of x',num1+1,num2+1)
        xx=float(input())
        X.append(xx)
    mat.append(X)
x=[1.]*n
lam1,vec1=eig1(mat,x)
print('Largest eigenvalue is:',lam1)
print('Respective eigenvector is:',vec1)
lam2,vec2=eig2(mat,lam1,vec1)
print('Largest eigenvalue is:',lam2)
print('Respective eigenvector is:',vec2)
