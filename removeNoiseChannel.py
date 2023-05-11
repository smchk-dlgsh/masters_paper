from textgrid import TextGrid

def remove_item_with_name(textgrid_file, item_name, output_file):
    tg = TextGrid()
    tg.read(textgrid_file)

    item_index_to_remove = None
    for i, item in enumerate(tg):
        if item.name == item_name:
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


remove_item_with_name('/Users/valeriia/stuff/STUDYING/YEAR_6/masters_degree/paired_plain_data/535530_2022_03_12_18_01_37_1_34.TextGrid',
                           'noise',
                           '535530_2022_03_12_18_01_37_1_34_WITHOUT_NOISE.TextGrid')


