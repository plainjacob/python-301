# Create a `Planet()` class that models attributes and methods of
# a planet object.
# Use the appropriate dunder method to get informative output with `print()`

class Planet():
    """Creates a planet object."""
    def __init__(self, name, radius, orbit):
        self.name = name
        self.radius = radius
        self.orbit = orbit

    def __str__(self):
        return f"The planet {self.name} has a radius of {self.radius} kilometers and orbits around the {self.orbit}."

p = Planet("Earth", 6371.0, "Sun")
print(p)