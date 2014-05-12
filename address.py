from base import Base
import random

class Address(Base):
    def __init__(self):
        self.street_addresses = self.get_file_data("street_addresses.txt")
        self.cities = self.get_file_data("cities.txt")
        self.states = self.get_file_data("states.txt")
        self.states_abbr = self.get_file_data("states_abbr.txt")

    def state(self):
        return random.choice(self.states)

    def state_abbr(self):
        return random.choice(self.states_abbr)

    def city(self):
        return random.choice(self.cities)

    def street_address(self):
        return random.choice(self.street_addresses)

    def zip_code(self):
        return random.randint(10000, 99999)

    def secondary_address(self):
        return "%s %s" % (random.choice(["Apt.", "Suite"]), random.randint(100, 999))

    def latitude(self):
        return str(random.uniform(1, 181) - 90)

    def longitude(self):
        return str(random.uniform(1, 361) - 180)
