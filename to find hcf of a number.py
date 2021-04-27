
def compute_hcf(x, y):
    if x<y:
        smaller=y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1 =int(input('enter an number 1 :'))
num2 =int(input('enter a number  2 :'))
print("The H.C.F. is", compute_hcf(num1, num2))
