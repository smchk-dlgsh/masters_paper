import argparse
import tgt 

def textgrid2rttm(textgrid):
    rttm_out = dict()
    tg = tgt.read_textgrid(textgrid, encoding="utf-8")

    for spkr in tg.get_tier_names():
        speaker_id = tg.get_tier_names().index(spkr)
        spkr_timestamps = []
      
        for _interval in tg.get_tiers_by_name(spkr):
            for interval in _interval:

                start, end, phrase = interval.start_time,\
                              interval.end_time,\
                              interval.text
        
                spkr_timestamps.append((start, end-start, phrase, speaker_id))

        rttm_out[spkr] = spkr_timestamps
    return rttm_out


def write_rttm(rttm_out, full_file_name):
    with open(full_file_name + '.rttm', 'w') as fout:
        for spkr in rttm_out:
            for start, dur, phrase, speaker_id in rttm_out[spkr]:
                fout.write(u'SPEAKER {} 1 {} {} <NA> <NA> {} <NA>\n'
                           .format(
                    full_file_name.split('/')[-1],
                    start,
                    dur,
                    full_file_name + '-' + str(speaker_id)
                    ))


if __name__ == '__main__':
    command_example = "python textgrid2rttm.py /folder/"
    parser = argparse.ArgumentParser(epilog=command_example)
    parser.add_argument('input_file',
                        help=''' Input File ''')
    parser.add_argument('output_file',
                        help='''Name of the output file in which to write''')

    args = parser.parse_args()

    rttm_out = textgrid2rttm(args.input_file)
    write_rttm(rttm_out, args.output_file)