# Write a script with three classes that model everyday objects.
# - Each class should have an `__init__()` method that sets at least 3 attributes
# - Include a `__str__()` method in each class that prints out the attributes
#     in a nicely formatted string.
# - Overload the `__add__()` method in one of the classes so that it's possible
#     to add attributes of two instances of that class using the `+` operator.
# - Create at least two instances of each class.
# - Once the objects are created, change some of their attribute values.
#
# Be creative. Have some fun. :)
# Using objects you can model anything you want:
# Animals, paintings, card games, sports teams, trees, people etc...

class Fish:
  """Creates a fish object."""
  def __init__(self, species, age):
    self.species = species
    self.age = age

  def __str__(self):
    return f"The fish is a {self.species.lower()} and is {self.age} years old."

class Candy:
  """Creates a candy object."""
  def __init__(self, name, amount):
    self.name = name
    self.amount = amount

  def __str__(self):
    return f"{self.name} ({self.amount})"

  def __add__(self, other):
    new_name = self.name + other.name
    new_amount = self.amount + other.amount
    return Candy(name=new_name, amount=new_amount)

class Painting:
  """Creates a painting object."""
  def __init__(self, name, artist, value):
    self.name = name
    self.artist = artist
    self.value = value

  def __str__(self):
    return f"The {self.name} is painted by {self.artist} and is valued at {self.value} dollars."

  def increase_value(self, increment):
    self.value += increment


f1 = Fish("Goldfish", 2)
f2 = Fish("Clownfish", 5)
print(f1)

c1 = Candy("Skittles", 5)
c2 = Candy("Twizzlers", 10)
c3 = c1 + c2
print(c3)