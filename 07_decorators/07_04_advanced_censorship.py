# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

import re

def censor(*words):
  def decorator(func):
    def wrapper(*args):
      nonlocal words

      new_args = []
      for arg in args:
        for word in words:
          match = re.search(word, arg, re.IGNORECASE)
          replacement = match.group()[0] + (len(word) - 1) * "*" 
          arg = re.sub(word, replacement, arg, flags=re.IGNORECASE)
        new_args.append(arg)
        func(*new_args)
    return wrapper
  return decorator

@censor("shoot", "crab")
def print_text(text):
  print(text)

if __name__ == "__main__":
  print_text("I bumped my toe! Shoot! Crab!")
