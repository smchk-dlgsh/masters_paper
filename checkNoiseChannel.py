import os
import chardet


folder_path = "/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/paired_plain_data" 
file_list = [f for f in os.listdir(folder_path) if f.endswith('.TextGrid')]
print(file_list)


# Iterate over each file
for file_name in file_list:
    file_path = os.path.join(folder_path, file_name)
    
    with open(file_path, 'rb') as file:
      raw_data = file.read()
      result = chardet.detect(raw_data)
      encoding = result['encoding']

    with open(file_path, 'r', encoding=encoding) as file:
      content = file.read().lower()
      if "noise" in content:
        print(f"{file_name} contains 'noise'")
      else:
        print(f"{file_name} does not contain 'noise'")
   
