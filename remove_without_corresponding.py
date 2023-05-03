import os

def remove_files_without_corresponding(directory):
    file_names = set()
    print('os.listdir(directory)', len(os.listdir(directory)))
    # for file in os.listdir(directory):
        # file_name, file_extension = os.path.splitext(file)

        # file_names.add(file_name)


        # print('file_name', file_name)
        # print('file_extension', file_extension)
        # new_name = file_name.replace('.', '_').replace('-', '_') + file_extension
        # os.rename(directory + '/' + file_name + file_extension,
        #           directory + '/' + new_name)
        # if ((file_name + '.wav') not in os.listdir(directory)) and ((file_name + '.TextGrid') not in os.listdir(directory)):
        #   file_path = os.path.join(directory, file)
        #   os.remove(file_path)
        #   print(f"to Remove {file_path}")
        # print(len(file_names))

# Specify the directory path
directory = "/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/test_plain_data"

# Call the remove_files_without_corresponding function
remove_files_without_corresponding(directory)
