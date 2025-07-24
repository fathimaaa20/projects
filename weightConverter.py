# Python Weight Converter
def convert_weight():
    try:
        weight = float(input("Enter your weight: "))
        unit = input("Enter the unit (kg/lb): ").strip().lower()

        if unit == 'kg':
            converted = weight * 2.205
            print(f"{weight:.2f} kg is equal to {converted:.2f} lb.")
        elif unit == 'lb':
            converted = weight / 2.205
            print(f"{weight:.2f} lb is equal to {converted:.2f} kg.")
        else:
            print("Invalid unit. Please enter 'kg' or 'lb'.")

    except ValueError:
        print("Please enter a valid number for weight.")

# Call the function
convert_weight()
