import numpy as np
import matplotlib.pyplot as plt

# Quadratic weather model function
def quadratic_weather_model(t, a, b, c):
    return a * t**2 + b * t + c

# Initial coefficients
a_base, b_base, c_base = -0.2, 1.5, 24

# Times to check temperature
times_to_check = [0, 6, 12, 18, 24]

# Number of increments
increments = 4

# Prepare smooth time array for plotting curves
time_smooth = np.linspace(0, 24, 200)

# Colors for plotting
colors = ['blue', 'green', 'red', 'purple']

plt.figure()

print("\n=== INCREMENT MODEL ===")

for inc in range(increments):
    print(f"\nIncrement {inc+1}:")
    
    # Simulate coefficient changes — example: increase a and decrease c over increments
    a = a_base + 0.05 * inc          # a increases slightly
    b = b_base                      # b constant
    c = c_base - 0.8 * inc          # c decreases
    
    # Print temperatures at specific times
    for t in times_to_check:
        temp = quadratic_weather_model(t, a, b, c)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    print("---")
    
    # Compute smooth curve temperatures
    temps_smooth = quadratic_weather_model(time_smooth, a, b, c)
    
    # Plot the curve
    plt.plot(time_smooth, temps_smooth, color=colors[inc], label=f'Increment {inc+1}')
    
    # Mark data points at times_to_check
    temps_points = [quadratic_weather_model(t, a, b, c) for t in times_to_check]
    plt.scatter(times_to_check, temps_points, color=colors[inc])

plt.title("Increment Model Temperature Prediction")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("increment_model_temperature.png")
plt.show()

