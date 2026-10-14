# type casting (explicit conversion) allows you to manually convert a variable from one data type to another using constructor functions like str(), int(), float(), bool(), list(), tuple(), set()

# explicit conversion examples from notes:
year = 2026 # int
year_as_string = str(year) # now 2026 (int) is "2026" (str)
country = str('South Africa')  # Explicitly define/cast as a string
gdp_growth_percentage_string = '0.9'
gdp_growth_percentage = float(gdp_growth_percentage_string)
has_nobel_peace_prize_winners = bool(1)  # 1 is an int now its converted to the boolean value True

print(country)
print(gdp_growth_percentage)
print(has_nobel_peace_prize_winners)

# explicit vs implicit conversion
# implicit conversion happens automatically when different data types are used together (e.g., int + float = float):
bill = 750 # int
tip_percent = 0.10 # float (10%)
tip = bill * tip_percent
total_bill = bill + tip # automatically implicitly converted to float
print(tip) # will print out 75.0
print(total_bill) # will print out 825.0
print(type(total_bill)) # Output: <class 'float'>

# explicit conversion is required when implicit conversion fails (e.g., string concatenation with numbers):
za_median_age = 28.9
za_median_age = str(za_median_age)
# trying to run print("The national median age of South Africa is " + (za_median_age) + " years.") will return a TypeError.
# instead, explicitly convert the float to a string:
statement = "The national median age of South Africa is " + za_median_age + " years." # make sure you add in those white spaces otherwise it'll print "...is28.9years" instead of "...is 28.9 years"
print(statement) # now za_median_age is a string and can be printed with the rest of the statement with no error

# casting strings to integers or floats
# if you have a string written as a numeric digit, then you can convert it to an int or a float:
za_climate_adaptation_index = "101"
za_climate_adaptation_index = int(za_climate_adaptation_index)
print(za_climate_adaptation_index) # this can be converted to an int. if it was written out in words like "one hundred and one", it will return a ValueError so make sure that the string is valid

za_average_salary = "30611.0"
za_average_salary = float(za_average_salary)
print(za_average_salary)

# we can specify how many decimal points should show but we'll look at that in numeric_types.py 

# casting float to integer (this will chop out the decimals after the whole number. its called truncation and truncation can apply to the beginning or end of something and can be used in multiple scenarios when coding, but in this context it is the ending decimals that are removed):
za_average_utility_costs = 1250.00
za_average_utility_costs = int(za_average_utility_costs)
print(za_average_utility_costs) # bye bye decimal points


# we can also do type casting with collections like from a list to a tuple/set but we'll look at that when we dive into the notes_collections folder