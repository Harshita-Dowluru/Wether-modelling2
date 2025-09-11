import matplotlib.pyplot as plt

# Quadratic weather model function
def quadratic_weather_model(t, a, b, c):
    return a * t**2 + b * t + c

# Coefficients for the quadratic function
a, b, c_base = -0.2, 1.5, 24

# Time points (hours)
hours = list(range(0, 25, 12))  # 0, 12, 24

# Number of iterations
iterations = 3

# Prepare plot
plt.figure()
colors = ['blue', 'green', 'red']

print("\n=== ITERATIVE MODE TEMPERATURE PREDICTIONS ===")

for i in range(iterations):
    # Simulate changing 'c' (intercept) in each iteration
    c = c_base - i * 0.5
    
    # Calculate temperatures at defined hours
    temperatures = [quadratic_weather_model(t, a, b, c) for t in hours]
    
    # Plot this iteration's temperatures
    plt.plot(hours, temperatures, marker='o', linestyle='-', color=colors[i], label=f'Iteration {i+1}')
    
    # Print values
    print(f"\nIteration {i+1}:")
    for t, temp in zip(hours, temperatures):
        print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")

plt.title("Iterative Model Temperature Prediction")
plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.legend()
plt.savefig("iterative_model.png")
plt.show()
