import os

def remove_files_with_extension(directory, extension):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)
            print(f"Removed {file_path}")

# Specify the directory path and extension
directory = "/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/RTTMs+WAVs"
extension = ".TextGrid"

# Call the remove_files_with_extension function
remove_files_with_extension(directory, extension)
