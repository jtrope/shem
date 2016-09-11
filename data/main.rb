require_relative 'get_data'

files_to_write = [
  "full_names",
  "email_suffixes",
  "cities",
  "street_addresses",
  "states",
  "states_abbr",
  "creating_conflict"
]

file_generator(files_to_write)
