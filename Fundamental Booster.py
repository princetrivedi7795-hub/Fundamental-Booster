# Interactive Personal Data Collector

print("=" * 55)
print("Welcome to the Interactive Personal Data Collector!")
print("=" * 55)

print("\nThis program collects your basic information")
print("and demonstrates Python variables, data types,")
print("operators, type casting, type() and id().")

# Collect Information
print("\n--- Enter Your Information ---")

name = input("Please enter your name: ")

age = int(input("Please enter your age: "))

height = float(input("Please enter your height in meters: "))

favourite_number = int(input("Please enter your favourite number: "))

# Data Processing
# Current year
current_year = 2026
# Calculate approximate birth year
birth_year = current_year - age

# Some arithmetic operations
double_age = age * 2
age_after_five_years = age + 5
half_age = age / 2
remainder = age % 2
# Display Results

print("\n" + "=" * 55)
print("Thank you! Here is the information we collected:")
print("=" * 55)

print(f"\nName: {name}")
print(f"Age: {age}")
print(f"Height: {height} meters")
print(f"Favourite Number: {favourite_number}")
# Data Type and Memory Address

print("\n--- Variable Details ---")

print(f"\nName:")
print(f"  Value: {name}")
print(f"  Data Type: {type(name)}")
print(f"  Memory Address: {id(name)}")

print(f"\nAge:")
print(f"  Value: {age}")
print(f"  Data Type: {type(age)}")
print(f"  Memory Address: {id(age)}")

print(f"\nHeight:")
print(f"  Value: {height}")
print(f"  Data Type: {type(height)}")
print(f"  Memory Address: {id(height)}")

print(f"\nFavourite Number:")
print(f"  Value: {favourite_number}")
print(f"  Data Type: {type(favourite_number)}")
print(f"  Memory Address: {id(favourite_number)}")
# Calculations

print("\n--- Data Processing Results ---")

print(f"Your approximate birth year is: {birth_year}")
print(f"Your age after 5 years will be: {age_after_five_years}")
print(f"Double of your age is: {double_age}")
print(f"Half of your age is: {half_age}")
print(f"Remainder when your age is divided by 2: {remainder}")
# Final Message

print("\n" + "=" * 55)
print("Thank you for using the Personal Data Collector!")
print("Keep learning and explore Python further.")
print("Goodbye!")
print("=" * 55)
