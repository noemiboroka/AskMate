def det_new_id(id_list):

    new_id = int(max(id_list)) + 1
    return new_id

def search_line(data_table, id):

    current_index = 0

    for row in data_table:
        if row[0] == id:
            index = current_index
        else:
            current_index += 1
    return index