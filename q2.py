from math import exp
import numpy as np
from romil import g_diff
from tran import tra
from gj import gj
x=[1]*5
E=lambda a,b,c,d,e: (a-20)+\
   (a+(0.25*b)+(c/16)+(d*exp(e/4))-51.58)**2+\
   (a+(b/2)+(c/4)+(d*exp(e/2))-68.73)**2+\
   (a+0.75*b+(9*c/16)+(d*exp(3*e/4))-75.36)**2+\
   (a+b+c+(d*exp(e))-74.36)**2+\
   (a+1.25*b+(25*c/16)+d*exp(1.25*e)-67.09)**2+\
   (a+1.5*b+2.25*c+(d*exp(1.5*e))-53.73)**2+\
   (a+1.75*b+(1.75**2*c)+(d*exp(1.75*e))-37.98)**2+\
   (a+2*b+4*c+d*exp(2*e)-17.28)**2
j1=lambda e:exp(0.25*e)
j2=lambda e:exp(0.5*e)
j3=lambda e:exp(0.75*e)
j4=lambda e:exp(e)
j5=lambda e:exp(1.25*e)
j6=lambda e:exp(1.5*e)
j7=lambda e:exp(1.75*e)
j8=lambda e:exp(2*e)
norm=1
ex=E(x[0],x[1],x[2],x[3],x[4])
k=0
while abs(norm)>1e-5 and k<500:
    k+=1
    a,b,c,d,e=x[0],x[1],x[2],x[3],x[4]
    J=[[1,1,1,1,1,1,1,1,1],[0,0.25,0.5,0.75,1,1.25,1.5,1.75,2],[0,1/16,0.25,0.75**2,1,1.25**2,1.5**2,1.75**2,4],[0,j1(e),j2(e),j3(e),j4(e),j5(e),j6(e),j7(e),j8(e)],[0,0.25*d*j1(e),0.5*d*j2(e),0.75*d*j3(e),d*j4(e),1.25*d*j5(e),1.5*d*j6(e),1.75*d*j6(e),2*d*j8(e)]]
    jj=np.matmul(J,tra(J))
    diag=[[jj[0][0]/0.01,0,0,0,0],\
          [0,jj[1][1]/0.01,0,0,0],\
          [0,0,jj[2][2]/0.01,0,0],\
          [0,0,0,jj[3][3]/0.01,0],\
          [0,0,0,0,jj[4][4]/0.01]]
    H=jj+diag
    x_temp=gj(H,g_diff(E,x))
    for nu in range(len(x)):
        x[nu]=x[nu]+x_temp[nu]
    e1=E(x[0],x[1],x[2],x[3],x[4])
    norm=e1-ex
    ex=e1
print(x)
