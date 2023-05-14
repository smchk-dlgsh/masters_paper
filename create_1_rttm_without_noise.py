import os

folder_path = '/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/NEMO_OUTPUT_with_NOISE/max_speaker_num=4/'
output_file = 'with_Noise_max_speaker_num=4.rttm' 
with open(output_file, 'w', encoding='utf-16-le', errors='ignore') as output:
    # Iterate over all files in the folder
    for file_name in os.listdir(folder_path):
        file_basename, file_extension = os.path.splitext(file_name)
        if file_extension == '.rttm':
          file_path = os.path.join(folder_path, file_name)
          # Open each file in binary mode
          with open(file_path, 'rb') as file:
              content = file.read().decode('utf-16-le', errors='ignore')
              output.write(content)