weight = float(input("Enter your weight: "))
unit = input("Enter the unit (kg/lb):").strip().lower()

if unit.lower() == 'kg':
    converted_weight =weight * 2.205
    print(f"{weight:.2f} kg is equal to {converted_weight:.2f}")
elif unit.lower() == 'lb':
    converted_weight = weight/2.205
    print(f"{weight:.2f} lb is equal to {converted_weight:.2f} kg.")
else:
    print("Invalid unit. Please enter 'kg' or 'lb'.")        