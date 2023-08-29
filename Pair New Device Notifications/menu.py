import os
import subprocess

# Get a list of all python files in the current directory
python_files = [f for f in os.listdir() if f.endswith('.py')]

# Exclude the script itself from the list if it's in the same directory
script_name = os.path.basename(__file__)
if script_name in python_files:
    python_files.remove(script_name)

# Ensure there are no more than 60 python files
if len(python_files) > 60:
    print("There are more than 60 Python scripts in the directory.")
    exit(1)

# Display files with numbers
for idx, file_name in enumerate(python_files, start=1):
    print(f"{idx}. {file_name}")

# Ask user for choice
choice = int(input("\nSelect a number to execute the corresponding script: "))

# Check if the choice is valid
if 0 < choice <= len(python_files):
    # Execute the selected script
    subprocess.run(["python", python_files[choice - 1]])
else:
    print("Invalid choice.")
