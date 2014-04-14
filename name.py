from base import Base
import random
import logging

class Name(Base):
    def __init__(self, file_name="full_names.txt"):
        self.names = self.get_file_data(file_name)
        self.name_titles = ["Dr.", "Mrs.", "Mr.", "Ms.", "Miss"]
        # self.file_line_count = 5;

    def name(self):
        """ return a random full name from data """
        return self.names[ self.generate_rand() ]

    def first_name(self):
        name_components = self.name().split()
        for component in name_components:
            """ filter out nonsensical names such as Dr, Mrs, etc."""
            if not component in self.name_titles:
                return component

    def generate_rand(self):
        return random.randint(0, len(self.names) - 1)
