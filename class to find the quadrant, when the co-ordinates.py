def quadrant(x, y): 
    if (x > 0 and y > 0): 
        print ("lies in First quadrant") 
  
    elif (x < 0 and y > 0): 
        print ("lies in Second quadrant") 
          
    elif (x < 0 and y < 0): 
        print ("lies in Third quadrant") 
      
    elif (x > 0 and y < 0): 
        print ("lies in Fourth quadrant") 
          
    elif (x == 0 and y > 0): 
        print ("lies at positive y axis") 
      
    elif (x == 0 and y < 0): 
        print ("lies at negative y axis") 
      
    elif (y == 0 and x < 0): 
        print ("lies at negative x axis") 
      
    elif (y == 0 and x > 0): 
        print ("lies at positive x axis") 
      
    else: 
        print ("lies at origin") 
  
# Driver code      
x = -5
y = -8
quadrant(x, y) 