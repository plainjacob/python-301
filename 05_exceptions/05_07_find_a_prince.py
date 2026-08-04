# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

from pathlib import Path
import re

class PrinceException(Exception):
  pass

global_path = Path("./05_exceptions/books")
files = global_path.glob("*.txt")
for file in files:
  with open(file, "r") as f:
    first_hundred_chars = f.read(100)
    match = re.search("Prince", first_hundred_chars)
    if match:
      print(f.name)
      raise PrinceException()