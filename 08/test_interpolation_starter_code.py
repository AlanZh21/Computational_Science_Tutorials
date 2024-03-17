# Author: L. van Veen, Ontario Tech U, 2024.
# Starter code for tutorial 8.
import numpy as np
import matplotlib.pyplot as plt
from poly_int import poly_int
def chebyshev_nodes(a,b,n):
    k = np.array(range(n))
    x = np.cos((2*k + 1) * np.pi / (2*n))
    return 0.5 * (b-a) * x  + 0.5 *(b+a)
# Test function (the Runge function):
def f(x):                   
    return 1.0/(1.0+x**2)

# Domain:
l = -10
r = 10
number_of_grid_points = (2*(np.ones(7-2))) ** np.arange(2,7,1)
number_of_grid_points = number_of_grid_points.astype(int)
# Grid for plotting:
n_plot =  1000                       # Insert number large enough for producing a smooth plot but not large enough to slow the script down.
x_out = np.linspace(l,r,n_plot) 

# Remember errors for an increasing number of nodes for plotting:
err = []

# Loop over increasing number of grid points:
for n in range(1,7):
    N = 2**n
    # x-values for interpolation:
    x = np.linspace(l,r,N)
    # x = chebyshev_nodes(l,r,N)
    # Corresponding y-values:
    y = f(x)
    # Compute the interpolant on the fine grid using our code:
    y_out = poly_int(x,y,x_out)
    plt.plot(x_out,f(x_out),'-k',label='function')
    plt.plot(x_out,y_out,'-r',label='interpolant')
    plt.ylim([f(l)-1.0,f(r)+1.0])
    plt.xlabel('x')
    plt.ylabel('function and interpolant')
    plt.title('%d equidistant nodes' % (N))
    plt.legend()
    plt.show()
    y = f(np.linspace(l,r,n_plot))
    e = np.absolute(y-y_out)
    err.append([N,max(e)])
    # plt.plot(x_out,e,'-r',label='error')
    # plt.xlabel('x')
    # plt.ylabel('interpolation error')
    # plt.title('%d equidistant nodes' % (N))
    # plt.show()

# Plot the error of interpolation versus the number of nodes:
err = np.asarray(err)
plt.loglog(err[:,0],err[:,1],'-*')
plt.show()
