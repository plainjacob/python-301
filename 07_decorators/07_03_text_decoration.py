# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(symbol):
  def decorator(func):
    row = symbol * 30

    def wrapper(*args):
      nonlocal row
      print(row) 
      func(*args)
      print(row)
    return wrapper
  return decorator

@decorate("-")
def print_text(text):
  print(text)

if __name__ == "__main__":
  print_text("Hello")
