# Starter code for tutorial 7, MATH/CSCI2072U, Onterio Tech U, 2024.
import numpy as np

# In: 1D arrays x and y of length n, the interpolation data.
# Out: array a of polynomial coefficients so that the interpolant is P(x)= a[0] + a[1] * x + ... + a[n] * x^n.
def intpl(x,y):
    n = np.shape(y)[0] - 1                   # Extract the polynomial order of interpolation.
    print(n)
    V = np.zeros((n+1,n+1))                   # Allocate (n+1) by (n+1) array for the Vandermonde Matrix.
    for i in range(n+1):
        V[i][0] = 1
        for j in range(1,n+1):
            V[i][j] = V[i][j-1] * x[i]                 # Assign elements of the Vandermonde matrix
            print("test1",V[i][j])
    print("test", V)
    c = np.linalg.cond(V,2)
    a = np.linalg.solve(V,y)                   # Solve for the coefficents (use our LUP module or np.linalg.solve).
    return a, c

x = np.array([
    [0],
    [1],
    [2]
])
y = np.array([
    [0],
    [1],
    [2]
])
print(intpl(x,y))