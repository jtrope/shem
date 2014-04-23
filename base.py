import logging
import re
import random

class Base(object):

  def get_file_data(self, file_path):
    file = self.open_file(file_path)
    """return non blank names from file"""
    data = []
    for line in file:
      if re.match(".+", line):
        data.append( line.rstrip() )
    file.close()
    return data

  def open_file(self, file_path):
    try:
      f = open("data/"+file_path, "r")
    except IOError:
      logging.error("Could not find file.")
    else:
      return f

  def generate_rand_num(self, array):
    """Generates a random integer in the range of 0 and
    the length of the parameter - 1)"""
    return random.randint(0, len(array) - 1)
