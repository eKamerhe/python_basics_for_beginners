from decimal import *

# numeric types tell the interpreter how numbers behave in calculations and memory.

# integers (int) are positive or negative whole numbers without decimals, of unlimited length
za_population = 65000000 # This is an integer data type (positive and negative whole numbers).
print(za_population)
print(type(za_population)) # Output: <class 'int'>

# floating point numbers (float) are positive or negative numbers containing one or more decimals
za_gdp_growth_percentage = float(0.9) # Explicitly define as a float
print(za_gdp_growth_percentage)
print(type(za_gdp_growth_percentage)) # Output: <class 'float'>

# to achieve exact mathematical precision, we can import Decimal and pass numbers as strings
print(0.1 + 0.2) # outputs 0.30000000000000004
za_fraction_one = Decimal('0.1')
za_fraction_two = Decimal('0.2')

print(za_fraction_one + za_fraction_two) # outputs exact precision: 0.3

# complex numbers are written with a "j" as the imaginary part
za_complex_indicator = 3j # Explicitly define as a complex number
print(za_complex_indicator)
print(type(za_complex_indicator)) # Output: <class 'complex'>


# arithmetic operators operate on numeric types (+, -, *, /, //, %, **)
# addition (+), subtraction (-), multiplication (*), division (/):
za_provinces_count = 9
za_official_languages = 11

example_addition = za_provinces_count + 2
example_subtraction = za_official_languages - 2
example_multiplication = za_provinces_count * 2
example_division = za_official_languages / 2

print(example_addition)
print(example_subtraction)
print(example_multiplication)
print(example_division)

# floor division (//) divides and rounds down to the nearest whole integer:
example_floor_division = 10 // 3
print(example_floor_division) # 3

# modulus (%) returns the remainder of a division:
example_modulus = 10 % 3
print(example_modulus) # 1

# exponentiation (**) raises a number to a power:
example_exponentiation = 10 ** 3
print(example_exponentiation) # 1000

# numeric type conversion
# you can convert integers to floats, floats to integers, and numbers to complex numbers
za_provinces = 9
provinces_to_float = float(za_provinces)
print(za_provinces)
print(provinces_to_float)


# float to integer (truncates/cuts off the decimal part, does not round):
za_repo_rate = 7.25
repo_rate_to_integer = int(za_repo_rate)
print(za_repo_rate)
print(repo_rate_to_integer)

# real number to complex:
int_to_complex = complex(za_provinces)
print(int_to_complex)


# built-in math functions for numeric types
# absolute value abs():
complex_example = 5j
complex_to_absolute = abs(complex_example)
print(complex_example)
print(complex_to_absolute)

# rounding round():
float_rounded_off = round(za_repo_rate)
print(float_rounded_off)

# power pow():
# the pow() function is used to calculate powers (exponents). 
# it does the exact same job as the double asterisk operator (**), but as a built-in function call.

# basic usage: pow(base, exponent)
# for example, calculating 2 to the power of 3 (2 * 2 * 2):
print(pow(2, 3)) # prints 8 (this is identical to writing 2 ** 3)

# variable example using scaling:
base_multiplier = 2
years_doubling = 4
print(pow(base_multiplier, years_doubling)) # prints 16 (2 to the power of 4)


# the secret feature: the third argument (modulo)
# unlike the ** operator, the pow() function can take an optional third argument: pow(base, exponent, modulo)
# this calculates (base ** exponent) % modulo in one efficient step. 
# for example, 2 to the power of 3, divided by 5, giving us the remainder:
print(pow(2, 3, 5)) # calculates (2 ** 3) % 5 -> 8 % 5, which leaves a remainder of 3