import numpy as np
import matplotlib.pyplot as plt

# Quadratic weather model function
def quadratic_weather_model(t, a, b, c):
    return a * t**2 + b * t + c

# Base coefficients
a, b, c_base = -0.2, 1.5, 24

# Times to check temps in each sprint
times_to_check = [0, 6, 12, 18, 24]

# Prepare smooth time values for plotting curves (0 to 24 hours)
time_smooth = np.linspace(0, 24, 100)

# Colors for sprints
colors = ['blue', 'green']

plt.figure()

print("\n=== AGILE MODE ===")

for sprint in range(1, 3):
    print(f"\nSprint {sprint}:")
    
    # Simulate sprint-specific change by adjusting 'c'
    c = c_base - 0.7 * (sprint - 1)
    
    # Calculate and print temps at specific times
    for t in times_to_check:
        temp = quadratic_weather_model(t, a, b, c)
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
    print("---")
    
    # Calculate smooth curve temps for plotting
    temps_smooth = quadratic_weather_model(time_smooth, a, b, c)
    
    # Plot curve for this sprint
    plt.plot(time_smooth, temps_smooth, color=colors[sprint - 1], label=f'Sprint {sprint}')
    # Also plot the points at times_to_check with markers
    temps_points = [quadratic_weather_model(t, a, b, c) for t in times_to_check]
    plt.scatter(times_to_check, temps_points, color=colors[sprint - 1])

plt.title("Agile Mode Temperature Prediction")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("agile_mode_temperature.png")
plt.show()
