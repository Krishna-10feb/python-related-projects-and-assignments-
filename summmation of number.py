num=int(input("enetr the summation to calculate :"))
if num<0:
    print("enter a positve number :")
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1
        print("the sum is :",sum)
        