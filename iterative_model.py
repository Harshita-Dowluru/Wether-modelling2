# WEATHER MODELING - ITERATIVE MODEL
# Quadratic model: T(t) = a*t^2 + b*t + c

# === Initial Setup ===
a = -0.2
b = 1.5
c = 24

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c

# === Iterative Development ===
print("=== ITERATIVE MODEL ===")

# We simulate 3 iterations of development
for iteration in range(1, 4):
    print(f"Iteration {iteration}:")
    for hour in range(0, 25, 12):  # check at 0, 12, 24 hrs
        temp = quadratic_weather_model(hour)
        print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
    print("---")
