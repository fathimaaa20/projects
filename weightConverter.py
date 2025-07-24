# Python Weight Converter
weight = float(input("Enter weight: "))
unit = input("Kg or Pound? (k or l): ")

if unit.lower() == 'k':
    converted_weight = weight * 2.205
    print(f"{weight} kg is equal to {converted_weight:.2f} pounds.")
elif unit.lower() == 'l':
    converted_weight = weight / 2.205
    print(f"{weight} pounds is equal to {converted_weight:.2f} kg.")
else:
    print("Invalid unit. Please enter 'k' for kg or 'l' for pounds.")
