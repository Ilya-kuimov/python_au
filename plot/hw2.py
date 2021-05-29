import numpy as np
import matplotlib.pyplot as plt

file1 = open("input.txt", "r")
x_vals=file1.readline()
x = [int(i) for i in x_vals.split()]
#y = [int(i) for i in y_vals.split()]
y = np.cos(x)
file1.close()

plt.scatter(x, y, label='name of legend', c='green', marker='*')
plt.plot(x, y, c='purple')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Name of Graph')
plt.legend()

plt.show()