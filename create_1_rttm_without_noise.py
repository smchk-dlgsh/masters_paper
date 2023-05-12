import os

folder_path = '/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/rttms_made_without_NOISE'
output_file = 'gold_standart.rttm' 
with open(output_file, 'w', encoding='utf-16-le', errors='ignore') as output:
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Open each file in binary mode
        with open(file_path, 'rb') as file:
            content = file.read().decode('utf-16-le', errors='ignore')
            output.write(content)