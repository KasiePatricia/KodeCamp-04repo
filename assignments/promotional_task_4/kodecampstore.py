import os
import subprocess

# create groups
def create_group(group_name: str):
  try:
    # command to create a group
    subprocess.run(["sudo", "groupadd",group_name], check=True)
    print(f"Group '{group_name}' created successfully.")
    return group_name

  except subprocess.CalledProcessError as e:
    print(f"Error creating group '{group_name}': {e}")
    return False


# create user
def create_user(username: str, password: str=""):
  try:
    # command to create a user
    subprocess.run(["sudo", "useradd", username], check=True)
    subprocess.run(["sudo", "passwd", password])
    return username

  except subprocess.CalledProcessError as e:
    print(f"Error creating user '{username}': {e}")
    return False


# assign user to groups
def assign_user_to_group(username: str, group_name: str):
  try:
    subprocess.run(["sudo", "usermod", "-aG", group_name, username])
    return True
  except subprocess.CalledProcessError as e:
    print(f"Error assigning user '{username}' to group '{group_name}': {e}")
    return False

# user create file and directories
def creating_file_and_directory(name_of_file: str, name_of_directory: str):
  root = "all_company_files"
  company_directories = [
    "Finance Budgets",
    "Contract Documents",
    "Business Projections",
    "Business Models",
    "Employee Data",
    "Company Vision And Mission Statements",
    "Server Configuration Scripts",
  ]

  if len(name_of_directory) < 1:
    print(
      "The directory should not be empty."
    )
    return False

  if str.title(name_of_directory) not in company_directories:
    print(
      f"The directory {name_of_directory} does not exist"
    )
    return False

  if not os.path.exists(root):
    os.mkdir(f'{root}')
    print(f"directory created in {os.getcwd()}")

  os.chdir(f'{root}')
  print(f"directory changed to {os.getcwd()}")

  if not os.path.exists(name_of_directory):
    os.mkdir(name_of_directory)
    print(f"directory created in {os.getcwd()}")

  os.chdir(name_of_directory)
  print(f"directory changed to {os.getcwd()}")

  if os.path.exists(name_of_file):
    print(
      f"The file {name_of_file} already exists."
    )
    return False


  with open(f'{name_of_file}.txt', "w") as file:
    file.write("Welcome my people! \n\n You can have a sit")
  return True
