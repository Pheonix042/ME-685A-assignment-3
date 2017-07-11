def tra(a):
    rr=mat=[[0 for col in range(len(a))] for row in range(len(a[0]))]
    for num1 in range(len(a)):
        for num2 in range(len(a[num1])):
            rr[num2][num1]=a[num1][num2]
    return rr
