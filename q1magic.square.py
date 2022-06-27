
i=0


i=0
c=[]
while i<3:
    j=0
    d=[]
    while j<3:
        magic=int(input("enter no."))
        d.append(magic)
        j=j+1
    c.append(d)
    # print(c)
    i=i+1
i=0
row_sum=[]
col_sum=[]
while i<len(c):
    j=0
    sum=0
    while j<len(c):
        sum=sum+c[i][j]
        # print(sum)
        j=j+1
    col_sum.append(sum)
    j=0
    sum2=0
    while j<len(c):
        sum2=sum2+c[j][i]
        j=j+1
    row_sum.append(sum2)
    i=i+1
val=row_sum[0]
i=0
row_col_equal=True
while i<len(row_sum):
    if(row_sum[i]!=val or col_sum[i]!=val):
        print("This is not a magic square")
        break
        # row_col_equal=False
    i=i+1
if row_col_equal:
    row=0
    sum=0
    sum2=0
    while row<len(c):
        col=0
        while col<len(c):
            if row==col:
                sum=sum+c[row][col]
            if row+col==3-1:
                sum2=sum2+c[row][col]
            col=col+1
        row=row+1
    if sum==sum2:
        print(sum,"magic ")
