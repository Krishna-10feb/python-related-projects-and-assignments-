import numpy as np
import matplotlib.pyplot as plt
 #Scores of different players on different dates 
N = 3
ind = np.arange(N) 
width = 0.25
  
xvals = [8, 9, 2]
bar1 = plt.bar(ind, xvals, width, color = 'r')
  
yvals = [10, 20, 30]
bar2 = plt.bar(ind+width, yvals, width, color='g')
  
zvals = [11, 12, 13]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')
  
plt.xlabel("Dates")
plt.ylabel('Scores')
plt.title("Players Score")
  
plt.xticks(ind+width,['2021Feb01', '2021Feb02', '2021Feb03'])
plt.legend( (bar1, bar2, bar3), ('Player1', 'Player2', 'Player3') )
plt.show()