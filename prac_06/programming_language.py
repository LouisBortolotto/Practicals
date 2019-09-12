class ProgrammingLanguage:

    def __init__(self, field="", typing="", reflection=True, year=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Add amount to the car's fuel."""
        if self.typing.upper() == "DYNAMIC":
            return True
        else:
            return False

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.field, self.typing, self.reflection,
                                                                           self.year)
