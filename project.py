import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
v0 = 20  # Enter your desired initial velocity in m/s

# Define a list of launch angles in degrees
theta_degrees = [30, 45, 60]

# Convert angles to radians
theta_radians = np.deg2rad(theta_degrees)

# Function to calculate y(x)
def calculate_y(x, theta):
    return np.tan(theta) * x - (g * x**2) / (2 * (v0 * np.cos(theta))**2)

# Calculate maximum horizontal distance for the largest angle
d_max = (v0**2 * np.sin(2*np.max(theta_radians))) / g

# Set the range of x-values
x_values = np.linspace(0, d_max * 1.2, 100)  # adjust the multiplier as needed for visibility

# Plotting
plt.figure(figsize=(8, 6))  # Set figure size
for theta_rad in theta_radians:
    y_values = calculate_y(x_values, theta_rad)
    plt.plot(x_values, y_values, label=f'{round(np.rad2deg(theta_rad))}°')  # Round the angle value to the nearest integer

plt.title('Trajectories of a Mass')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.ylim(0, max(y_values) * 1.2)  # Set y-axis limits from 0 to maximum y-value
plt.legend(title='Launch Angle')
plt.grid(True)
plt.show()
