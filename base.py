import logging
import re

class Base(Conflict2):
  def get_file_data(self, file_path):
    """returns list of non blank names from file"""
    file = self.open_file(file_path)
    data = []
    for line in file:
      if re.match(".+", line):
        data.append( line.rstrip() )
    file.close()
    return data

  def open_file(self, file_name):
    """tries to open and return a file in the "./data" directory"""
    try:
      f = open("data/"+file_name, "r")
    except IOError:
      logging.error("Could not find file %s." % (file_name))
    else:
      return f
