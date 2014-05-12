require "faker"

def file_generator(files)
  # Takes an array of files to write
  # collects data from Faker and write to file
  files.each do |file_name|
    write_file(file_name)
  end
end

def write_file(file_name)
  seen_data = {}
  file = File.open("#{file_name}.txt", "w")
  5000.times do
    if file_name == "full_names"
      data = Faker::Name.name
    elsif file_name == "email_suffixes"
      data = Faker::Internet.email.match(/@.+/)[0]
    elsif file_name == "cities"
      data = Faker::Address.city
    elsif file_name == "street_addresses"
      data = Faker::Address.street_address
    elsif file_name == "states"
      data = Faker::Address.state
    elsif file_name == "states_abbr"
      data = Faker::Address.state_abbr
    else
      puts "#{file_name} does not exist."
    end

    if seen_data[data].nil?
      file << "#{data}\n"
    end
    seen_data[data] = true
  end
  file.close
end
