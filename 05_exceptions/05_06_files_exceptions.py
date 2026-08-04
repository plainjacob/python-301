# In this exercise, you will practice both File I/O as well as using Exceptions
# in a real-world scenario.
#
# This folder contains another folder called `books/` that contains three text files
# of books from Project Gutenberg:
# 1. war_and_peace.txt
# 2. pride_and_prejudice.txt
# 3. crime_and_punishment.txt
#
# 1) Open `war_and_peace.txt`, read the whole file content and store it in a variable
# 2) Open `crime_and_punishment.txt` and overwrite the whole content with an empty string
# 3) Loop over all three files and print out only the first character each. Your program
#    should NEVER terminate with a Traceback.
#     a) Which exception can you expect to encounter? Why?
#     b) How do you catch it to avoid the program from terminating with a traceback?


from pathlib import Path
# open war and peace
with open("05_exceptions/books/war_and_peace.txt", "r") as file:
  content = file.readlines()

# open crime and punishment
with open("05_exceptions/books/crime_and_punishment.txt", "w") as file:
  file.write("")

# loop over files
global_path = Path("./05_exceptions/books")
files = global_path.glob("*.txt")
for file in files:
  with open(file, "r") as f:
    first_line = f.readline()
    if len(first_line) > 0:
      first_char = first_line[0]
      print(first_char)