from romil import bi,check
fun='x**4-14*x**3+60*x**2-70*x'#str(input('enter polynomial'))
x1=float(input('Enter starting of interval:'))
x2=float(input('Enter ending of intrtval:'))
y1,y2=x1,x2
x=bi(fun,x1,x2)
val=check(fun,x,y1,y2)
print('Minimum value of function is:',val)
