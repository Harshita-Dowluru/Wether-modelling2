# WEATHER MODELING - INCREMENTAL MODEL
# Quadratic model: T(t) = a*t^2 + b*t + c

def quadratic_weather_model(a, b, c, t):
    """Predict temperature using quadratic equation."""
    return a * (t ** 2) + b * t + c

print("=== INCREMENTAL MODEL ===")

# === Increment 1: Hardcoded values ===
print("\nIncrement 1: Hardcoded values")
a, b, c, t = 0.5, -3, 28, 5
print(f"Inputs: a={a}, b={b}, c={c}, t={t}")
print(f"Predicted Temp: {quadratic_weather_model(a, b, c, t):.2f}°C")

# === Increment 2: Keyboard input ===
print("\nIncrement 2: Keyboard input")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time t (hour/day): "))
print(f"Predicted Temp: {quadratic_weather_model(a, b, c, t):.2f}°C")

# === Increment 3: File input (single set) ===
print("\nIncrement 3: File input (single set)")
with open("inputs_single.txt", "r") as f:
    lines = f.readlines()
a = float(lines[0]); b = float(lines[1]); c = float(lines[2]); t = float(lines[3])
print(f"File Inputs -> a={a}, b={b}, c={c}, t={t}")
print(f"Predicted Temp: {quadratic_weather_model(a, b, c, t):.2f}°C")

# === Increment 4: File input (multiple sets) ===
print("\nIncrement 4: File input (multiple sets)")
with open("inputs_multiple.txt", "r") as f:
    for line in f:
        a, b, c, t = map(float, line.strip().split())
        T = quadratic_weather_model(a, b, c, t)
        print(f"Inputs: a={a}, b={b}, c={c}, t={t} -> Predicted Temp: {T:.2f}°C")
