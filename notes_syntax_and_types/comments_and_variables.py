# comments and variables are foundational concepts in Python.
# data types are classifications that tell the interpreter how you intend to use a piece of data.

# 1. comments
    # single-line comments start with a hash symbol (#). Python ignores everything after # on that line. Consider these in-code notes for anyone reading the code, like you right now

        # there's no true multi-line comments in python but we can use triple-quotes (just dont assign them to anything)
        # technically these are just strings that python evaluates and throws away, so they're a handy trick rather than real comments
        # both """ and ''' work exactly the same way, but """ is the convention so we'll stick with that
        # a triple-quoted string that comes FIRST in a file/function/class becomes its docstring (more on those later)

"""
hi there! This is an example of a multi-line comment:

this wont show on the console when you run the terminal
"""


# 2. variables
    # variables are labels (names) that point to data values. The value itself lives separately in memory, the variable is just the name pointing at it. A variable is created the moment you first assign a value to it.
    # you can think of it like this: the variable is your hand, the value is the cup you're holding. you can swap cups without the cup changing (more on this in section 6)
country = "South Africa" # This is a string data type. You can also use single quotes for strings
population = 65400000 # This is an integer data type (positive and negative whole numbers).

# you print out the values of variables using the print() function
print(country)
print(population)

# python decides the data type based on the value assigned to the variable.
# you do not need to declare types upfront, and variables can change type after being set. we'll see more about that in type_casting.py


# 3. variable naming rules
    # variable names MUST START WITH a letter or an underscore (_)
    # CANNOT START WITH a number
    # CAN ONLY CONTAIN letters, numbers and underscores (A-Z, a-z, 0-9, and _).
    # variable names are case-sensitive (this means that country, Country, and COUNTRY are three DIFFERENT variables).
    # you CANNOT use python keywords as names (e.g., class, for, if, True). they're reserved for python itself


# 4. naming conventions (snake_case)
    # multi-word variable names in Python typically use snake_case (lowercase words separated by underscores):
za_median_age = 28.9
gdp_growth_percentage = float(0.9) # its wise for you to name variables in a way that should the code be passed on to someone else, they must easily understand what their purposes are

    # a note on prefixes: by convention, names starting with is_ or has_ (e.g., is_alive) signal a True/False value.
    # if the variable holds a name or a number, pick a name that says what it actually holds


# 5. multiple assignment & unpacking
# we can assign the same value to multiple variables in one line:
gdp_growth_rate_ivory_coast = gdp_growth_rate_tanzania = gdp_growth_rate_senegal = 6 # dont take my word on that number, this is an example
print(gdp_growth_rate_ivory_coast) # will print 6
print(gdp_growth_rate_tanzania) # will print 6
print(gdp_growth_rate_senegal) # will print 6

# heads up: this is safe here because integers are immutable. all three names point to the same 6 and none of them can change it, they can only be reassigned
# with a MUTABLE value like a list, all the names would share one list and a change through one name shows up in the others (see section 6)

# assign multiple values to multiple variables in one line:
currency, rand_to_dollar_rate = "ZAR", 0.06
print(currency) # will print ZAR
print(rand_to_dollar_rate) # will print 0.06

# creating a collection is called 'packing', and when you extract those values into variables, this is called 'unpacking':
za_presidents_1989_to_1999 = (
    "Frederik Willem de Klerk (1989-1994)", 
    "Nelson Mandela (1994-1999)"
    ) # this is a tuple

(national_party_president, anc_president) = za_presidents_1989_to_1999
print(national_party_president) # the first value is assigned to national_party_president
print(anc_president) # the second value is assigned to anc_president

# without an asterisk, the number of variables must match the number of values otherwise you will get an error
# you can assign multiple values to one variable by attaching an asterisk(*) to the variable that should hold the remaining values 
# the starred variable ALWAYS ends up as a list, even though the source here is a tuple
za_presidents_1994_to_2018 = (
    "Nelson Mandela (1994-1999)", 
    "Thabo Mbeki (1999-2008)", 
    "Kgalema Motlanthe (2008-2009)", 
    "Jacob Zuma (2009-2018)"
    )

(first_president, *later_presidents) = za_presidents_1994_to_2018
print(first_president) # the first value is assigned to first_president
print(later_presidents) # the remaining values are all assigned to later_presidents, as a list

# you can also add another variable after the asterisk, this will assign all the values to the one with an asterisk except for the last one which will be assigned to the remaining one
za_presidents_1994_to_present = (
    "Nelson Mandela (1994-1999)", 
    "Thabo Mbeki (1999-2008)", 
    "Kgalema Motlanthe (2008-2009)", 
    "Jacob Zuma (2009-2018)",
    "Cyril Ramaphosa (2018-present)"
    )

(first_president, *middle_presidents, latest_president) = za_presidents_1994_to_present
print(first_president) # will print out Mandela only
print(middle_presidents) # will print out Mbeki, Motlanthe and Zuma
print(latest_president) # will print out Ramaphosa only

# the starred variable is allowed to be empty, in which case it becomes an empty list []
(only_president, *nobody_else) = ("Nelson Mandela (1994-1999)",)
print(nobody_else) # will print []


# 6. mutability vs immutability (memory vs variable reassignment)
    # the word mutable comes from the word mutate (to change or transform).
    # mutable = can be modified in place inside memory without changing its memory address (e.g., lists, dictionaries, sets).
    # immutable = cannot be changed internally once created in memory (e.g., strings, integers, floats, tuples).

    # mutability belongs to the OBJECT (the value), not the variable. a variable can point to anything, it's the thing being pointed at that is either changeable or not.
    # the same variable can point to a list (mutable) now and a string (immutable) later

# REASSIGNMENT IS NOT MUTATION:
    # reassignment means making a variable label to point to a completely different value.
    # this is like putting down a cup of black coffee and picking up a cup of rooibos tea instead.
current_president = "Jacob Zuma"
current_president = "Cyril Ramaphosa" # valid: we didn't alter "Jacob Zuma", we just moved the variable label to a brand new string

# IMMUTABILITY IN ACTION (a sealed coffee pod):
    # you cannot reach inside an immutable object to modify its internal characters or items.
    # you can't change the coffee inside a sealed pod. if you want a different coffee, you need a brand new pod (a new object).
za_code = "ZAR"
# za_code[0] = "U" # TypeError: 'str' object does not support item assignment

# MUTABILITY IN ACTION (an open coffee mug):
    # with mutable data types, you can reach inside the existing container and add, remove, or swap items without creating a new object.
    # this is like adding milk or sugar into that same exact coffee mug sitting in our hand.
za_minings = ["Gold", "Diamonds", "Coal"] # this is a list
za_minings[0] = "Platinum" # valid: the original list changes in place to ["Platinum", "Diamonds", "Coal"]
za_minings.append("Iron Ore") # valid: adds "Iron Ore" into the same list container
print(za_minings)

# THE GOTCHA (two hands holding the same mug):
    # if two variables point to the same mutable object, changing it through one name is visible through the other.
    # there's only ONE mug, both names are just holding it.
mining_list_a = mining_list_b = ["Gold", "Coal"]
mining_list_b.append("Platinum") # we changed the list through mining_list_b...
print(mining_list_a) # ...but it shows up in mining_list_a too: ['Gold', 'Coal', 'Platinum']
    # if you want two separate mugs, make a copy instead: mining_list_c = mining_list_a.copy()

# THE CATCH (a sealed pod with a mug inside):
    # a tuple is immutable, but if it CONTAINS a mutable object like a list, that inner list can still be changed.
    # the tuple still points to the same list, it's just the list's contents that changed.
za_mining_info = ("Mining", ["Gold", "Coal"])
za_mining_info[1].append("Platinum") # valid: we changed the list inside, not the tuple itself
print(za_mining_info) # will print ('Mining', ['Gold', 'Coal', 'Platinum'])
# za_mining_info[0] = "Farming" # TypeError: 'tuple' object does not support item assignment