# Build on your freeform exercise from the previous section.
# Create child classes of two of the existing classes. Create a child class
# of one of the child classes so that the hierarchy is at least three levels.
#
# Build these classes out step-by-step like you did in the previous exercises.
# Use your notebook to brainstorm ideas and scribble down ideas.
#
# If you cannot think of a way to build on your freeform exercise,
# you can start with a new class from scratch.
# Try to make up your own example for this exercise, but if you are stuck,
# you could start working on the following:
#
# - A `Vehicle()` parent class, with `Truck()` and `Motorcycle()` child classes.
# - A `Restaurant()` parent class, with `Gourmet()` and `FastFood()` child classes.

class Vehicle:
  def __init__(self, wheels, weight):
    self.wheels = wheels
    self.weight = weight

class Truck(Vehicle):
  def __init__(self, wheels, weight, trailer):
    super().__init__(wheels, weight)
    self.trailer = trailer

class Motorcycle(Vehicle):
  def __init__(self, weight):
    self.weight = weight
    self.wheels = 2

car = Vehicle(4, 1500)
truck = Truck(6, 3000, False)
motor = Motorcycle(500)
