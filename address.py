from base import Base
import random

class Address(Base):
    def __init__(self):
        self.street_addresses = self.get_file_data("street_addresses.txt")
        self.cities = self.get_file_data("cities.txt")

    def city(self):
        return random.choice(self.cities)

    def street_address(self):
        return random.choice(self.street_addresses)

    def zip_code(self):
        return random.randint(10000, 99999)

    def secondary_address(self):
        return "%s %s" % (random.choice(["Apt.", "Suite"]), random.randint(100, 999))
