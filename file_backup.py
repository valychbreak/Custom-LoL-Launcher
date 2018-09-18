
def backup_original_file(original_file_path):
    original_file = open(original_file_path, "r")
    backup_file = open(original_file_path + ".backup", "w")

    backup_file.write(original_file.read())

    original_file.close()
    backup_file.close()
