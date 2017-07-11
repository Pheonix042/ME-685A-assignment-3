print('For the given system equation of motion is given by:')
print('2q(1)" + 2q(1) -q(2)=0')
print('3q(2)" - q(1) + q(3)=0')
print('4q(3)" - q(2) + q(3)=0')
from romil import eig1,eig2
from math import sqrt
mat=[[2,-1,0],[-1,0,1],[0,-1,1]]
x=[1.,1.,1.]
lam1,vec1=eig1(mat,x)
f1=sqrt(lam1/2)
print(f1,vec1)
lam2,vec2=eig2(mat,lam1,vec1)
f2=sqrt(lam2/3)
print(f2,vec2)
lam3,vec3=eig2(mat,lam2,vec2)
f3=sqrt(lam3/4)
print(f3,vec3)
