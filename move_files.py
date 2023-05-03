import os
import shutil

def move_files(source_folder, destination_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(source_path, destination_path)
            print(f"Moved {source_path} to {destination_path}")

# Specify the source folder and destination folder paths

### moving from Textgrid folder
# source_folder = "/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/TextGrid"
# destination_folder = "/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/plain_data"

source_folder = "/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/TextGrid"
destination_folder = "/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/plain_data"

# Call the move_files function
move_files(source_folder, destination_folder)
