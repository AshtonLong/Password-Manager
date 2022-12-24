import json

# This is a password manager and generator

# Define the dictionary
passwords = {}

def write_to_file():
  # Open the file in write mode
  with open("passwords.txt", "w") as file:
    # Convert the dictionary to a JSON string
    json_data = json.dumps(passwords)
    # Write the JSON string to the file
    file.write(json_data)

def read_from_file():
  # Open the file in read mode
  with open("passwords.txt", "r") as file:
    # Read the contents of the file
    json_data = file.read()
    # Check if the file is empty
    if len(json_data) > 0:
      try:
        # Parse the JSON string and convert it back to a dictionary
        passwords.update(json.loads(json_data))
      except json.decoder.JSONDecodeError:
        print("Error: Invalid JSON data in file")
    else:
      print("Error: File is empty")

def get_input():
  program = input("Please enter the program name: ")
  username = input("Please enter your email/username: ")
  password = input("Please enter your password: ")
  program = program.lower()

  # Add the values to the dictionary
  passwords[program] = {
    "username": username,
    "password": password
  }
  # Write the updated dictionary to the file
  write_to_file()

def search_info():
  see = input("Please enter the program you'd like to get info for: ")
  see = see.lower()
  if see in passwords:
    print(passwords[see])

def get_random():
  print("This will come soon!")

def get_remove():
  c_remove = input("Please enter the program you'd like to remove: ")
  c_remove = c_remove.lower()
  if c_remove in passwords:
    del passwords[c_remove]
    # Write the updated dictionary to the file
    write_to_file()

def get_programs():
  for program in passwords:
    print(program)

def main_menu():
  # Read the dictionary from the file
  try:
    read_from_file()
  except FileNotFoundError:
    # Create the file if it does not exist
    with open("passwords.txt", "w") as file:
      pass

  print("")
  print("1 for a random password")
  print("2 for adding a password")
  print("3 for searching a password")
  print("4 for removing a password")
  print("5 to quit")
  print("6 to find the existing programs")
  print("")
  choice = input("Please enter what you'd like to do: ")
  print("")
  if choice == "1":
    get_random()
  elif choice == "2":
    get_input()
  elif choice == "3":
    search_info()
  elif choice == "4":
    get_remove()
  elif choice == "5":
    exit()
  elif choice == "6":
    get_programs()
  else:
    print("You've entered an invalid number, please try again.")
  main_menu()

while True:
  main_menu()