from textgrid import TextGrid

def remove_item_with_name(textgrid_file, item_name, output_file):
    tg = TextGrid()
    tg.read(textgrid_file)

    item_index_to_remove = None
    for i, item in enumerate(tg):
        if item.name.lower() == item_name:
            item_index_to_remove = i
            break

    if item_index_to_remove is None:
        print(f"No item named '{item_name}' found in the TextGrid file.")
        return

    # Remove the item by reconstructing the TextGrid object
    new_tg = TextGrid()
    for i, item in enumerate(tg):
        if i != item_index_to_remove:
            new_tg.append(item)

    # Save the modified TextGrid file
    new_tg.write(output_file)


# remove_item_with_name('/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/paired_plain_data/535530_2022_03_12_18_01_37_1_34.TextGrid',
#                            'noise',
#                            '535530_2022_03_12_18_01_37_1_34_WITHOUT_NOISE.TextGrid')


import os

def process_textgrid_files(folder_path, item_name):
    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".TextGrid"):
            # Create the full file path
            file_path = os.path.join(folder_path, filename)

            # Generate the output file path

            # Remove the item with the specified name from the TextGrid file
            remove_item_with_name(file_path, item_name, filename)

# Example usage
folder_path = '/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/TG_without_NOISE/'
item_name = 'noise'
process_textgrid_files(folder_path, item_name)
