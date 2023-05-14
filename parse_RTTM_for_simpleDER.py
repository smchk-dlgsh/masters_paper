import simpleder

# PARSING GOLD RTTM for SIMPLE DER lib
gold_RTTM = open("gold_standart.rttm", "r")
rttm_array = gold_RTTM.read().splitlines()

def compareRTTM(rttm_basename):
      
  # filling the dict with the data: '535530_2022_03_17_07_03_27_1_34': ('1', 72.0951, 5.002939999999995)
  GOLD_ARRAY = []

  for file_line in rttm_array:
      line = file_line.split(' ')

      fileID = line[1]
      if fileID == rttm_basename:
        start_timestamp = float(line[3])
        duration = float(line[4])
        end_timestamp = start_timestamp + duration
        speakerID = line[7].split('-')[1]
        res_tuple = (speakerID, start_timestamp, end_timestamp)
        GOLD_ARRAY.append(res_tuple)

  print( 'GOLD dict for ' + rttm_basename,  GOLD_ARRAY)


  # PARSING NEMO RTTM OUTPUT 
  test_Nemo_RTTM = open('/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/NEMO_OUTPUT_without_noise/standart_dataset/' +  rttm_basename + '.rttm','r')
  nemo_array = test_Nemo_RTTM.read().splitlines()

  # filling the dict with the result data
  single_file_dict = {}
  single_recording_array = []

  for file_line in nemo_array:
      fileID = line[1]
      line = file_line.split(' ')
      start_timestamp = float(line[5])
      duration = float(line[8])
      end_timestamp = start_timestamp + duration
      speakerID = line[11]
      res_tuple = (start_timestamp, end_timestamp, speakerID)
      single_recording_array.append(res_tuple)

  error = simpleder.DER(GOLD_ARRAY, single_recording_array)

  print("DER={:.3f}".format(error))
  return error

print(compareRTTM('535530_2022_03_12_17_45_19_1_34'))