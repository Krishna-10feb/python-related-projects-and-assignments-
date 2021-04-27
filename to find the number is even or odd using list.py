#to find the number is even or odd 
list1 = [10, 21, 4, 45, 66, 93] 
num = 0
  
# using while loop         
while(num < len(list1)): 
      
    # checking condition 
    if num % 2 == 0: 
       print(list1[num], end = " ") 
      
    # increment num   
    num += 1
     