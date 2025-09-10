# WEATHER MODELING - WATERFALL MODEL
# Quadratic model: T(t) = a*t^2 + b*t + c

# === Requirement Analysis ===
# Inputs: coefficients a, b, c and time t
# Output: Predicted temperature

# === System Design ===
a = -0.2
b = 1.5
c = 24

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c

# === Implementation & Testing ===
print("=== WATERFALL MODEL ===")
for hour in range(0, 25, 6):  # every 6 hours
    temp = quadratic_weather_model(hour)
    print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")

# === Deployment ===
print("Model executed successfully. Ready for deployment.")
