gold_RTTM = open("gold_standart.rttm", "r")
rttm_array = gold_RTTM.read().splitlines()

dict = {}
 # filling the dict with the data: '535530_2022_03_17_07_03_27_1_34': ('1', 72.0951, 5.002939999999995)
 
for file_line in rttm_array:
    line = file_line.split(' ')

    fileID = line[1]
    start_timestamp = float(line[3])
    duration = float(line[4])
    speakerID = line[7].split('-')[1]

    dict[fileID] = (speakerID, start_timestamp, duration )

print(dict)