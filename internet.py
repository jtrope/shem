from name import Name
import random

class Internet(Name):
    def __init__(self):
        super(Internet, self).__init__()
        self.email_suffixes = self.get_file_data("email_suffixes.txt")

    def email(self, name=None):
        email_suffix = random.choice(self.email_suffixes)
        if name:
            return self.get_email_prefix(name) + email_suffix
        else:
            return self.get_email_prefix(random.choice(self.names)) + email_suffix

    def domain_name(self):
        return random.choice(self.email_suffixes)[1::]

    def domain_word(self):
        """return the company name component of an email address"""
        domain_word = ""
        for char in self.domain_name():
            if char != ".":
                domain_word += char
            else:
                break
        return domain_word

    def domain_suffix(self):
        """example return values: com, info, biz"""
        domain_suffix = random.choice(self.email_suffixes)
        dot_idx = domain_suffix.index(".")
        return domain_suffix[dot_idx+1::]

    def free_email(self):
        free_emails = ["@gmail", "@yahoo", "@aol", "@hotmail"]
        return self.get_email_prefix(random.choice(self.names)) + random.choice(free_emails)

    def user_name(self):
        return self.get_email_prefix(random.choice(self.names))

    def get_email_prefix(self, name):
        """takes a name and turns it into email format.
        Args: the string representing the name
        Returns: the reversed string seperated by .
        """
        valid_names = [n for n in name.split() if not n in (self.suffixes + self.prefixes)]
        return ".".join(valid_names[::-1]).lower()
