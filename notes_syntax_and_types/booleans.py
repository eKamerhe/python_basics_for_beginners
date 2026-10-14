# booleans represent one of two values: True or False. They are used to evaluate logical expressions and conditions
# python spells them with capitals: True and False. Lowercase true/false raises a NameError

# existing code: defined implicitly or explicitly
# bool() is for CONVERTING other values to a boolean. True is already a boolean, so it isn't needed here
has_nobel_peace_prize_winners = True
print(has_nobel_peace_prize_winners)
print(type(has_nobel_peace_prize_winners)) # Output: <class 'bool'>

# comparison operators return boolean values (True or False)
number_1 = 5
number_2 = 5
number_3 = 5.01

# equal to (==): is what's on the left THE SAME value as what's on the right?
print(number_1 == number_2) # True
print(number_1 == number_3) # False

# not equal to (!=): is what's on the left NOT THE SAME value as what's on the right?
print(number_1 != number_2) # False
print(number_1 != number_3) # True

# greater than (>): is what's on the left GREATER THAN the value on the right?
print(number_1 > number_2) # False
print(number_3 > number_1) # True

# less than (<): is what's on the left LESS THAN the value on the right?
print(number_1 < number_2) # False
print(number_3 < number_1) # False

# greater/lesser than or equal to (>= and <=, respectively): is what's on the left GREATER/LESSER THAN OR EQUAL TO the value on the right?
print(number_1 >= number_2) # True
print(number_1 <= number_2) # True
print(number_3 >= number_1) # True
print(number_3 <= number_1) # False

# chained comparisons: python lets you chain them (Java and C# don't)
x = 7
print(0 < x < 10)  # True (same as 0 < x and x < 10)
print(1 < 5 < 3)   # False (5 < 3 is False)

# logical operators combine boolean expressions
# python uses the words and / or / not instead of && / || / !

# and (returns True if ALL statements are true):
print(number_1 == number_2 and number_1 < number_3) # True
print(number_1 != number_2 and number_1 < number_3) # False

# or (returns True if AT LEAST ONE statement is true):
print(number_1 != number_2 or number_1 < number_3) # True
print(number_1 != number_2 or number_1 > number_3) # False

# not (flips the boolean value of the result). It's an operator, not a function, so brackets only group:
print(not (number_1 != number_2)) # True
print(not (number_1 == number_2)) # False

# order of evaluation: not first, then and, then or
print(not 0 and "yes")  # yes (not 0 is True, then True and "yes" gives "yes")

# and / or don't always return True or False: they return one of the OPERANDS (the values either side)
# short-circuiting: and stops at the first falsy value, or stops at the first truthy value
print(0 or "default")        # default (0 is falsy, so or moves on to the next value)
print("Nelson" or "default")  # Nelson (first value is truthy, so or stops there)
print("Nelson" and 5)        # 5 (first value is truthy, so and moves on and returns the last value)
print(0 and 5)               # 0 (first value is falsy, so and stops there)

# truthy vs falsy: python's built-in way of checking if something has content or if it's empty/zero/None
# falsy values:
print(bool(0))        # False because if my balance is 0, then I have no money
print(bool(0.0))      # False because it's a zero float
print(bool(""))       # False because the string is empty
print(bool([]))       # False because the list is empty
print(bool({}))       # False because the dictionary is empty
print(bool(()))       # False because the tuple is empty
print(bool(set()))    # False because the set is empty
print(bool(None))     # False because None means "no value"

# truthy values (python evaluates everything else as True because "something is there"):
print(bool(25))        # True because the value is not zero
print(bool(-3))        # True because negative numbers are not zero either
print(bool("Nelson"))  # True because the string isn't empty
print(bool("False"))   # True because the string isn't empty, whatever it says
print(bool("0"))       # True because the string isn't empty
print(bool([1, 2]))    # True because the list isn't empty

# gotcha: truthiness can't tell 0 apart from None. In market data, 0 is a real value and None means missing
price = 0
missing_price = None
print(price is None)          # False (0 is a real value)
print(missing_price is None)  # True (the value is missing)
# is checks IDENTITY (is it the very same object?), == checks VALUE. Use "is None" to check for missing data