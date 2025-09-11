# version3_file_input_single.py
# Predict temperature using coefficients and time read from a file (single set)

input_filename = "inputs_single.txt"

try:
    with open(input_filename, "r") as f:
        lines = f.readlines()

    # Strip and convert lines to floats
    a = float(lines[0].strip())
    b = float(lines[1].strip())
    c = float(lines[2].strip())
    t = float(lines[3].strip())

    # Calculate temperature using quadratic formula
    T = a * t**2 + b * t + c

    # Print results
    print("=== FILE INPUT (SINGLE SET) TEMPERATURE PREDICTION ===")
    print(f"Read from file '{input_filename}':")
    print(f"a = {a}, b = {b}, c = {c}, t = {t}")
    print(f"Predicted temperature at t = {t} → T = {T:.2f}°C")

except FileNotFoundError:
    print(f"❌ Error: File '{input_filename}' not found.")
except IndexError:
    print(f"❌ Error: File '{input_filename}' does not contain enough data.")
except ValueError:
    print(f"❌ Error: File '{input_filename}' contains invalid data.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
