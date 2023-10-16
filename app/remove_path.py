def process_string_data(string_path):
    string_path = str(string_path)
    processed_string = string_path.split("//")[1]
    return processed_string