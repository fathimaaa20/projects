unit = input("Is temperature in Celsius or Fahrenheit (C/F): ").strip().upper()
temp = float(input("Enter the temparature: "))

if unit == 'C':
    converted_temp =round((temp* 9/5)+32,1)
    print(f"{temp} celsius is equal to {converted_temp} fahrenheit")
elif unit == 'F':
    converted_temp =round((temp-32)*5/9,1)
    print(f"{temp} fahrenheit is equal to {converted_temp} celsius")
else:
    print("f{unit} is invalid unit of measurement")
    