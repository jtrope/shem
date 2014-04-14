class Name(object):
  def open_file(self):
    f = open("data/full_names.txt", "r")
    for line in f:
      print line
