# version4_file_input_multiple.py
# Predict temperature using multiple sets of coefficients and time read from a file

input_filename = "inputs_multiple.txt"

try:
    with open(input_filename, "r") as f:
        lines = f.readlines()

    print("=== FILE INPUT (MULTIPLE SETS) TEMPERATURE PREDICTION ===")
    for idx, line in enumerate(lines, start=1):
        if line.strip():  # skip empty lines
            # Parse values from line
            a, b, c, t = map(float, line.strip().split())

            # Calculate temperature
            T = a * t**2 + b * t + c

            # Print results
            print(f"Set {idx}: a={a}, b={b}, c={c}, t={t} -> T={T:.2f}°C")

except FileNotFoundError:
    print(f"❌ Error: File '{input_filename}' not found.")
except ValueError:
    print(f"❌ Error: File '{input_filename}' contains invalid data or wrong format.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
