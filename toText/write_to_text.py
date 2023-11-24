from utilities.extract import text


def write_string_to_file(input_string, file_name):
    try:
        with open(file_name, 'w') as file:
            for char in input_string:
                file.write(f"{ord(char)}\n")
        print(f"Values written to {file_name} successfully.")
    except Exception as e:
        print(f"Error: {e}")


write_string_to_file(text, "output.txt")
