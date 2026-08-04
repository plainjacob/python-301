# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'

try:
  with open(f"05_exceptions/{file_name}", "r") as file:
    try: 
      first_number = int(file.readline())
      print(first_number + first_number)
    except ValueError:
      print("First line is not a number.")
except FileNotFoundError:
  print("File is not found.")
