import os

def process_files_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.TextGrid'):
            base_name, _ = os.path.splitext(file_name)
            rttm_file = base_name + '.rttm'
            textgrid_file = os.path.join(folder_path, file_name)
            output_folder_path = '/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/rttms_made_of_TextGrids'
            output_file = os.path.join(output_folder_path, base_name)
            os.system(f"python textgrid2rttm.py {textgrid_file} {output_file}")

# Specify the folder path
folder_path = "/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/textGrids_to_be_converted_into_RTTM"

# Call the process_files_in_folder function
process_files_in_folder(folder_path)
