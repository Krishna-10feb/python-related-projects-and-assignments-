from matplotlib import pyplot as plt 
#ages of labour 

ages_x =[25,23,26,34,56]

dev_y =[20000,23000,24000,40000,46000]
plt.plot(ages_x,dev_y,'k--', marker ='.',label='all devs')

py_dev_y = [40000,50000,80000,90000,110000]
plt.plot(ages_x,py_dev_y,'r', marker = '+', label ='python')

js_dev_y =[60000,50000,65000,70000,80000]
plt.plot(ages_x,js_dev_y,'b',marker ='*', label ='java script')

plt.xlabel('ages of the employees (years)')
plt.ylabel('salary per month ')
plt.title('age v/s salary')

plt.tight_layout()
plt.grid(True)
plt.savefig("test.png")
plt.show()