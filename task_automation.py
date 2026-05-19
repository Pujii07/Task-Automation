# Task Automation with Python
# Move all JPG files from one folder to another

import os
import shutil

# Source folder path
source_folder = input("Enter source folder path: ")

# Destination folder path
destination_folder = input("Enter destination folder path: ")

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Counter
count = 0

# Check files in source folder
for file in os.listdir(source_folder):

    # Check if file is JPG
    if file.endswith(".jpg"):

        source_path = os.path.join(source_folder, file)

        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(file, "moved successfully")

        count += 1

print("\nTotal files moved:", count)

print("Task completed successfully!")