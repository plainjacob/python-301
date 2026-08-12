# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

import re

def censor(func):
  def wrapper(*args):
    new_args = []
    for arg in args:
      result = re.search(r"([Ss])hoot", arg)
      if result:
        new_args.append(arg.replace(result.group(), f"{result.group(1)}****"))
    func(*new_args)
  return wrapper

@censor
def print_text(text):
  print(text)

if __name__ == "__main__":
  print_text("I bumped my toe! Shoot!")