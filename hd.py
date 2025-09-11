# version1_hardcoded.py
# Predict temperature using hardcoded coefficients

# Hardcoded coefficients
a = 0.5
b = -3
c = 28

# Hardcoded time
t = 5  # Example: 5th hour or 5th day

# Calculate temperature
T = a * t**2 + b * t + c

# Output the result
print("=== HARDCODED TEMPERATURE PREDICTION ===")
print(f"Using equation: T(t) = {a}·t² + ({b})·t + {c}")
print(f"Predicted temperature at t = {t} → T = {T:.2f}°C")
