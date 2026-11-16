import numpy as np
import matplotlib.pyplot as plt

# Domain and Function

x = np.linspace(-10, 10, 20)

def f(x):
    return  (1/10) *x ** 2

y = f(x)

def dfdx(x):
    return x / 5

# Initial Conditions

x0 = x[17]
y0 = f(x0)
dy0 = dfdx(x0)

# Gradient Descent Parameters

eta = 0.01

tol = 1e-2

error = np.abs(dy0)

iterations = 0 

plt.ion()

fig, ax = plt.subplots()
point, = ax.plot([x0], [y0], 'ro')  # Plot the initial point



# Gradient Descent Loop

while error > tol:
    x0 = x0 - eta * dy0
    y0 = f(x0)
    error = np.abs(y0)
    dy0 = dfdx(x0)
    iterations += 1
    point.set_data([x0], [y0])  #
    ax.plot(x0, y0, 'ro')
    plt.pause(0.01)

p = print("Converged in", iterations, "iterations")
p
plt.ioff()
plt.plot(x, y)  # Plot the original function for reference
plt.plot([x0], [y0], 'ro')  # Plot the final point
plt.title("Gradient Descent on Parabolic Function",print(p))
plt.show()