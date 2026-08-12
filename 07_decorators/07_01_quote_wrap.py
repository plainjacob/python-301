# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def quote(func):
  def wrapper(*args):
    new_args = [f'"{arg}"' for arg in args]
    func(*new_args)
  return wrapper

@quote
def print_text(text):
  print(text)

if __name__ == "__main__":
  print_text("Hello world!")
