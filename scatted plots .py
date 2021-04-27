import matplotlib.pyplot as pyplot
 
# data
a = [2,4,6,8,10,11,11.5,11.7]
b = [1,1.5,2,2.5,3,3.5,4,4.5]
ab=[8,8.5,9,9.5,10,10.5,11]
cd=[3,3.5,3.7,4,4.5,5,5.2]
 
# matplotlib plot
pyplot.scatter(a,b,label='Scatter Plot 1',color='r')
pyplot.scatter(ab,cd,label='Scatter Plot 2',color='b')
pyplot.xlabel('some x label')
pyplot.ylabel('some y label')
pyplot.title('Scatter Plot Example')
pyplot.legend()
pyplot.show()