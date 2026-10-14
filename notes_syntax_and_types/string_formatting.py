# string formatting allows you to interpolate variables and expressions directly into text strings

za_country_name = "South Africa"
za_president = "Cyril Ramaphosa"
za_presidents_1989_to_present = ("de Klerk, Mandela, Mbeki, Motlanthe, Zuma, Ramaphosa")
dirty_string = "   Eskom   "
za_population = 65000000
za_gdp_growth_percentage = 0.9
za_median_age = 28.9
za_unemployed_people = 8500000
za_labour_force = 25200000

# 1. string concatenation (+)
# string concatenation is when we link/join separate thing together in a series or chain
# we can concatenate strings by using the + oeprator and we have to account for the white spaces ourselves otherwise the words will glue to each other
print(za_president + " is the president of " + za_country_name) # good
print(za_president + "is the president of" + za_country_name) # bad ("...Ramaphosais...ofSouth...")

# here's an example with explicit casting involved:
full_statement = za_country_name + " has a za_population of approximately " + str(za_population) + " and a GDP growth rate of " + str(za_gdp_growth_percentage) + "%."
print(full_statement)


# 2. f-strings (formatted string literals)
# f-strings automatically convert non-strings and insert them directly into text using {variable_name}
# this saves us the manual white-spacing effort and looks cleaner
full_statement_fstring_version = f"{za_country_name} has a za_population of approximately {za_population} and a GDP growth rate of {za_gdp_growth_percentage}%."
print(full_statement_fstring_version)

# we can also run expressions inside f-strings. 
# we can perform arithmetic operations inside {}, for example:
print(f"The unemployment rate in South Africa is {za_unemployed_people / za_labour_force * 100}%") 
# we can also specify how many decimal points we want to show by adding a colon (:) a full stop (.) the number decimal points we want and the letter f like so:
print(f"The unemployment rate in South Africa is {za_unemployed_people / za_labour_force * 100:.2f}%") # :.2f means we want 2 decimal points
# we can also round off to the nearest whole number using the round() built-in function, for example:
print(f"The unemployment rate in South Africa is {round(za_unemployed_people / za_labour_force * 100)}%")

# string methods are built-in functions that allow us to manipulate/search/format/check properties of text sequences, for example:
print(f"Use .upper() to convert strings to upper case. e.g. {za_country_name} becomes {za_country_name.upper()}.") 
print(f"Use .lower() to convert strings to lower case. e.g. {za_president} becomes {za_president.lower()}.")
print(f"Use .index() to find the index position of the letter 'a' in {za_president} which is {za_president.index('a')}.")
print(f"Use .replace() to change the president from {za_president} to {za_president.replace('Cyril', 'Matamela Cyril', 1)}.") # .replace ("what you want to change", "what you want to change it to" , how many occurances it should change)
print(f"Use .strip() to remove all leading and trailing white-spaces from a string variable. e.g. {dirty_string} becomes {dirty_string.strip()}.")
print(f"Use .startswith() to check if a word starts with a specific value, this will return true or false. e.g. It is {za_country_name.startswith('S')} that the variable za_country_name starts with the letter 'S'. ") # true
print(f"Use .zfill to add 0 to the beginning of a variable until the full variable characters reach your desired number of characters. e.g. {za_country_name.zfill(20)}") # dont do this with other data types, you will get an AttributeError
print(f"Use .split() to split a string into a list. e.g. '{za_presidents_1989_to_present}' becomes {za_presidents_1989_to_present.split(', ', 3)}")
# important things to note about .split()
    # 1. EMPTY BRACKETS .split()
        # Cuts everywhere there is a space. It drops the spaces, but leaves commas glued to words:
        # 'de Klerk, Mandela' becomes ['de', 'Klerk,', 'Mandela']

    # 2. MATCHING CHARACTER .split(', ')
        # Cuts everywhere it finds a comma followed by a space. Cleans out the commas and gives clean names:
        # 'de Klerk, Mandela' becomes ['de Klerk', 'Mandela']

    # 3. WITH A LIMIT .split(', ', 3)
        # Cuts at the first 3 comma-spaces only. Leaves you with 4 items total (the first 3 names, plus 1 big chunk at the end holding whatever is left)

# for more info on lists go to lists.py

# thousands separators for large numbers (e.g., :,):
print(f"{za_population:,}") # using :, we can put commas in long numbers (>= 1000), this makes them easier to read 


# 3. legacy formatting methods (we don't write code like this, its old-school. we only need to know it in case we encounter 'ancient' code)
# %-formatting (%s for strings, %d for ints, %f for floats):
print("The president of %s is %s." % (za_country_name, za_president)) # %s = string placeholder, % (values) fills them in left to right

# str.format() method ("{}".format(val)):
print("The president of {} is {}.".format(za_country_name, za_president)) # {} are placeholders, .format() fills them in left to right