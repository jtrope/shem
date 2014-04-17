import logging
import re

class Base(object):
  def __init__(self):
    self.prefixes = ["Dr.", "Mrs.", "Mr.", "Ms.", "Miss"]
    self.suffixes = ["DDS", "Jr.", "Sr.", "DVM", "PhD", "MD", "V", "IV", "I", "II", "III"]

  def get_file_data(self, file_path):
    file = self.open_file(file_path)
    """Add non blank lines to array"""
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
      logging.error("Could note find file.")
    else:
      return f
