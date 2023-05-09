import os
import re
from dataclasses import dataclass
from typing import Any

NEMO_OUTPUT = """
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   8.537   1.092 <NA> <NA> speaker_1 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   9.728   1.265 <NA> <NA> speaker_0 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   10.993   1.042 <NA> <NA> speaker_1 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   12.060   3.101 <NA> <NA> speaker_0 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   16.625   2.208 <NA> <NA> speaker_1 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   19.305   1.886 <NA> <NA> speaker_0 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   22.460   2.580 <NA> <NA> speaker_1 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   25.338   2.605 <NA> <NA> speaker_0 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   28.961   2.878 <NA> <NA> speaker_1 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   31.839   1.638 <NA> <NA> speaker_0 <NA> <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1   33.675   4.120 <NA> <NA> speaker_1 <NA> <NA>
"""

RTTM_OUTPUT = """
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 9.72756465443025 1.2653844829367404 <NA> <NA> *р* любимка <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 12.05984193670581 1.04208133888908 <NA> <NA> мы переехали <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 13.10192327559489 0.7195323530424602 <NA> <NA> *нерозб* <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 13.82145562863735 1.3398188642859612 <NA> <NA> в ближайшее время не будет <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 19.30478838802989 1.8856709941802414 <NA> <NA> *нерозб* <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 25.338174700847517 2.6052033462294695 <NA> <NA> да ну вроде завтра как на беларусь уйдём <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 30.275655328463365 1.5631220077376788 <NA> <NA> ну всё ладно <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 31.838777336201044 1.6375563890585205 <NA> <NA> давай всё целую пока <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 8.53661455284273 1.0917042597885604 <NA> <NA> *р* да папуль <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 10.99294913736699 1.04208133888908 <NA> <NA> *ім* <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 16.625150659457972 2.208219980026861 <NA> <NA> а куда переехали то далеко <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 22.460045289774964 2.580391885789183 <NA> <NA> *роз* а ну всё равно на Украине да <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 28.96064792512849 2.8285064901919945 <NA> <NA> ну хорошо ладно *о* хорош <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 33.674825408781814 1.2901959428945915 <NA> <NA> всё давай пока целую <NA>
SPEAKER 926315_2022_03_28_17_33_39_2_110 1 34.7169067472736 3.078093252726404 <NA> <NA> *шт* <NA>
"""

@dataclass
class SpeakerRange:
    started_at_ms: int
    ended_at_ms: int
    speaker: str

def parse_nemo(input_text: str) -> list[SpeakerRange]:
    speaker_ranges: list[SpeakerRange] = []

    lines = input_text.splitlines()
    lines = list(filter(lambda line: line != "", lines))
    for line in lines:
        line += "\n" # Adding endline symbol to help regex match correctly
        match = re.search("^([^\s]+\s+){3}([^\s]+)\s+([^\s]+)\s+([^\s]+\s+){2}([^\s]+\s)(.+\s+){2}$", line)
        if match is None:
            print("ALERT REGEX HAS NOT MATCHED:", line)
            continue
        
        started_at, duration, speaker = match.group(2), match.group(3), match.group(5)
        
        started_at_ms = int(float(started_at) * 1000)
        ended_at_ms = started_at_ms + int(float(duration) * 1000)
        speaker = speaker.strip()
        speaker_range = SpeakerRange(started_at_ms, ended_at_ms, speaker)
        
        speaker_ranges.append(speaker_range)
    
    return speaker_ranges


@dataclass
class TextRange:
    started_at_ms: int
    ended_at_ms: int
    text: str

def parse_annotation(input_text: str) -> list[TextRange]:
    text_ranges: list[TextRange] = []

    lines = input_text.splitlines()
    lines = list(filter(lambda line: line != "", lines))
    for line in lines:
        line += "\n" # Adding endline symbol to help regex match correctly
        match = re.search("^([^\s]+\s+){3}([^\s]+\s+)([^\s]+\s+)(.*)<NA>\s+(.+)\s+<NA>$", line)
        if match is None:
            print("ALERT REGEX HAS NOT MATCHED:", line)
            continue
        
        started_at, duration, text = match.group(2), match.group(3), match.group(5)
        
        started_at_ms = int(float(started_at) * 1000)
        ended_at_ms = started_at_ms + int(float(duration) * 1000)
        text = text.strip()
        text_range = TextRange(started_at_ms, ended_at_ms, text)
        
        text_ranges.append(text_range)
    
    return text_ranges

@dataclass
class TextSpeakerRange:
    started_at_ms: int
    ended_at_ms: int
    text: str
    speakers: list[str]

def merged_speaker_data(nemo_ranges: list[SpeakerRange], text_ranges: list[TextRange]) -> list[TextSpeakerRange]:
  
    def range_intersection(text_range: TextRange, speaker_range: SpeakerRange) -> bool:
        return max(
            text_range.started_at_ms,
            speaker_range.started_at_ms,
        ) <= min(
            text_range.ended_at_ms,
            speaker_range.ended_at_ms,
        )
    
    textspeaker_ranges: list[TextSpeakerRange] = []

    for text_range in text_ranges:
        speaker_ranges_intersected_with_text_range = filter(
            lambda nemo_range: range_intersection(text_range, nemo_range),
            nemo_ranges
        )
        speakers = set(
            speaker_range.speaker 
            for speaker_range in speaker_ranges_intersected_with_text_range
        )
        
        textspeaker_range = TextSpeakerRange(
            started_at_ms=text_range.started_at_ms,
            ended_at_ms=text_range.ended_at_ms,
            text=text_range.text,
            speakers=list(speakers),   
        )
        textspeaker_ranges.append(textspeaker_range)
    
    return textspeaker_ranges

def read_filenames_from_flat_directory(dirpath: str) -> list[str]:
    for _, __, filenames in os.walk(dirpath):
        return filenames
    
def read_file(filepath: str) -> str:
    with open(filepath) as file:
        return file.read()

def main() -> None:
    ROOT_DIR = "/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree"
    NEMO_DIR = f"{ROOT_DIR}/rttms_NeMo"
    ANNOTATIONS_DIR = f"{ROOT_DIR}/rttms_made_of_TextGrids"

    results: dict[str, list[TextSpeakerRange]] = {}

    annotations_filenames = read_filenames_from_flat_directory(ANNOTATIONS_DIR)
    for annotation_filename in annotations_filenames:
        print('annotation_filename', annotation_filename)
        annotation_file = read_file(f"{ANNOTATIONS_DIR}/{annotation_filename}")
        nemo_file = read_file(f"{NEMO_DIR}/{annotation_filename}")

        nemo_ranges = parse_nemo(nemo_file)
        text_ranges = parse_annotation(annotation_file)

        textspeaker_ranges = merged_speaker_data(nemo_ranges, text_ranges)

        filename_without_extension = ".".join(annotation_filename.split(".")[:-1])
        results[filename_without_extension] = textspeaker_ranges
    
    def dump_to_json() -> None:
        dict_data = {}
        for filename, result in results.items():
            dict_data[filename] =  {
                "words": [
                    {
                        "started_at": r.started_at_ms / 1_000,
                        "duration": (r.ended_at_ms / 1_000) - (r.started_at_ms / 1_000),
                        "speakers": r.speakers,
                        "text": r.text,
                    }
                    for r in result
                ]
            }

        from json import dump
        with open('./OUTPUT.json', 'w', encoding='utf8') as file:
          dump(dict_data, file, ensure_ascii=False)
    
    dump_to_json()

main()