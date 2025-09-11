import matplotlib.pyplot as plt

# Waterfall model quadratic temperature prediction function
def waterfall_temperature(t):
    a, b, c = -0.2, 1.5, 24
    return a * t**2 + b * t + c

# Define time points (hours)
hours = list(range(0, 25, 6))  # 0, 6, 12, 18, 24

# Calculate temperatures for each hour
temperatures = [waterfall_temperature(t) for t in hours]

# Plot the temperature over time
plt.plot(hours, temperatures, marker='o', linestyle='-', color='blue')
plt.title("Waterfall Model Temperature Prediction")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.savefig("waterfall_model.png")  # Save plot as PNG file
plt.show()

# Print values for each time point
print("=== WATERFALL MODEL TEMPERATURE PREDICTION ===")
for t, temp in zip(hours, temperatures):
    print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
