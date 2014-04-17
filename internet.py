from name import Name
import logging

class Internet(Name):
    def __init__(self, file_names={"email_suffixes" : "email_suffixes.txt", "full_names" : "full_names.txt"}):
        try:
            self.email_suffixes = self.get_file_data(file_names["email_suffixes"])
            self.names = self.get_file_data(file_names["full_names"])
        except KeyError:
            logging.error("Options hash key does not exist.")
        super(Name, self).__init__()

    def email(self, name=None):
        pass
