import os
from kodecampstore import create_group, create_user, assign_user_to_group, creating_file_and_directory

# Task 1
def store_employees():
  employees_data = {
    "IT_TEAM": [("Andrew", "System Administrator"), ("Gozie", "IT intern")],
    "LEGAL_TEAM": [("Julius", "Legal")],
    "HR_TEAM": [("Chizi", "Human Resource Manager")],
    "SALES_TEAM": [("Jeniffer", "Sales Manager")],
    "BUSINESS_TEAM": [("Adeola", "Business Strategist"), ("Bach", "CEO")],
    "FINANCE_TEAM": [("Ogochukwu", "Finance Manager")],
  }

  for team, employees in employees_data.items():
    group_name = create_group(team)
    if not group_name:
      continue
    print(f"Group '{group_name}' created successfully.")

    for name, role in employees:
      user_data = create_user(name,"")
      if not user_data:
        continue
      print(f"User {user_data} created successfully.")

      assign_user_to_group(user_data, group_name)
      print(
        f"User {user_data} assigned to group '{group_name}' successfully."
      )

    print(f"user data: {user_data} belongs to group named: {group_name}, ")


# Task 2
def task_2():    
  file_name = input("Input The name of your file: ")
  directory = input("Input the directory you want to create your file: ")

  creating_file_and_directory(file_name, directory)


def main():
  task_2()
  store_employees()

main()