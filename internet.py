from name import Name
import random

class Internet(Name):
    def __init__(self):
        super(Internet, self).__init__()
        self.email_suffixes = self.get_file_data("email_suffixes.txt")

    def email(self, name=None):
        email_suffix = self.email_suffixes[ self.generate_rand_num(self.email_suffixes) ]
        if name:
            return self.get_email_prefix(name) + email_suffix
        else:
            return self.get_email_prefix(self.names[ self.generate_rand_num(self.names) ]) + email_suffix

    def get_email_prefix(self, name):
        valid_names = [ n for n in name.split() if not n in (self.suffixes + self.prefixes) ]
        return ".".join(valid_names[::-1]).lower()
