# WEATHER MODELING - AGILE MODEL
# Quadratic model: T(t) = a*t^2 + b*t + c

# === Initial Setup ===
a = -0.2
b = 1.5
c = 24

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c

# === Agile Development in Sprints ===
print("=== AGILE MODEL ===")

times_to_check = [0, 6, 12, 18, 24]  # key times in the day

# Sprint 1: Deliver basic functionality
print("Sprint 1:")
for t in times_to_check:
    temp = quadratic_weather_model(t)
    print(f"Time: {t} hrs -> Predicted Temp: {temp:.2f}°C")
print("---")

# Sprint 2: Deliver improved/tested version
print("Sprint 2:")
for t in times_to_check:
    temp = quadratic_weather_model(t)
    print(f"Time: {t} hrs -> Predicted Temp: {temp:.2f}°C")
print("---")
