require_relative 'get_data'

files_to_write = [
  "full_names",
  "email_suffixes",
  "cities",
  "street_addresses",
  # "us_states",
  #"us_states_abbr"
]

file_generator(files_to_write)
