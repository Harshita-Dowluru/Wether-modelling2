# version2_keyboard_input.py
# Predict temperature using keyboard input for coefficients and time

print("=== KEYBOARD INPUT TEMPERATURE PREDICTION ===")

try:
    # Take input from the user
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    t = float(input("Enter time t (hour/day): "))

    # Calculate the temperature using the quadratic formula
    T = a * t**2 + b * t + c

    # Display the result
    print(f"\nUsing equation: T(t) = {a}·t² + ({b})·t + {c}")
    print(f"Predicted temperature at t = {t} → T = {T:.2f}°C")

except ValueError:
    print("❌ Invalid input. Please enter numeric values only.")
