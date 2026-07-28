# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car:
  """Creates a car object."""
  def __init__(self, model, year, max_speed):
    self.model = model
    self.year = year
    self.max_speed = max_speed

  def __str__(self):
    return f"The {self.model} has gone into production in the year {self.year} and has a maximum speed of {self.max_speed} miles per hour."

  def increase(self):
    self.max_speed += 5

c1 = Car("BMW iX3 (NA5)", 2025, 130)
print(c1)
c1.increase()
print(c1)
c2 = Car("Nissan Sentra", 1982, 124)