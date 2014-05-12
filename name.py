from base import Base
import re
import random

class Name(Base):
    def __init__(self, file_name="full_names.txt"):
        self.prefixes = ["Dr.", "Mrs.", "Mr.", "Ms.", "Miss"]
        self.suffixes = ["DDS", "Jr.", "Sr.", "DVM", "PhD", "MD", "V", "IV", "I", "II", "III"]
        self.names = self.get_file_data(file_name)

    def first_name(self):
        """filters out prefixes and returns first name"""
        name_components = self.__split_name()
        return [component for component in name_components if not component in self.prefixes][0]

    def suffix(self):
        return random.choice(self.suffixes)

    def prefix(self):
        return random.choice(self.prefixes)

    def last_name(self):
        potential_last_name = self.__split_name()[-1]
        if potential_last_name in self.suffixes:
            return self.last_name()
        return potential_last_name

    def name(self):
        """ return a random full name from data """
        return random.choice(self.names)

    def __split_name(self):
        return self.name().split()
