# -*- coding: utf-8 -*-
"""Finite Difference.ipynb

Automatically generated by Colaboratory.

"""

import numpy as np
import matplotlib.pyplot as plt

def solve_poisson_equation(N, L, alpha, beta, f):
    dx = L / (N - 1)
    x = np.linspace(0, L, N)
    phi = np.zeros(N)
    phi[0] = alpha
    phi[-1] = beta
    A = np.diag(-2 * np.ones(N)) + np.diag(np.ones(N - 1), 1) + np.diag(np.ones(N - 1), -1)
    A /= dx**2
    b = f(x)
    b[0] -= alpha / dx**2
    b[-1] -= beta / dx**2
    phi[1:-1] = np.linalg.solve(A[1:-1, 1:-1], b[1:-1])
    return x, phi

# Example: Solve Poisson equation with f(x) = 1, alpha = 0, beta = 0, L = 1
N = 100
L = 1.0
alpha = 0.0
beta = 0.0
def f(x):
    return np.ones_like(x)
x, phi = solve_poisson_equation(N, L, alpha, beta, f)
plt.plot(x, phi, label='Numerical Solution')
plt.xlabel('x')
plt.ylabel('phi(x)')
plt.title('Numerical Solution of Poisson Equation')
plt.legend()
plt.show()