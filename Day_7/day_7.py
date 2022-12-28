from sys import maxsize


# directory_history: FILO list of directory names
def parse_command(line: str, directory_files_table: dict[str, list[str]],
                  directory_history: list[str], current_dir: str):
    if line[0:2] == "cd":
        if line[3:] == "..":
            current_dir = directory_history.pop()
            return current_dir
        elif line[3:] not in directory_files_table:
            full_path = ""
            if current_dir != "":
                if len(directory_history) == 0:
                    full_path = current_dir + "/" + line[3:]
                else:
                    full_path = "/".join(
                        directory_history) + "/" + current_dir + "/" + line[3:]
            else:
                full_path = line[3:]
            directory_files_table[full_path] = []
        if current_dir != "":
            directory_history.append(current_dir)
        current_dir = line[3:]
    return current_dir


def parse_line(line: str, directory_files_table: dict[str, list[str]],
               file_size_table: dict[str, int], directory_history: list[str],
               current_dir: str):
    if line[0] == "$":
        current_dir = parse_command(line[2:], directory_files_table,
                                    directory_history, current_dir)
        return current_dir
    else:
        (filesize, filename) = line.split(" ")
        full_directory_path = ""
        if current_dir != "/":
            full_directory_path = "/".join(
                directory_history) + "/" + current_dir
        else:
            full_directory_path = "/"
        if filename not in directory_files_table[full_directory_path]:
            filepath = full_directory_path + "/" + filename
            directory_files_table[full_directory_path].append(filepath)
            if filesize == "dir":
                file_size_table[filepath] = -1
            else:
                file_size_table[filepath] = int(filesize)
    return current_dir


def compute_directory_size(directory_full_path: str,
                           directory_files_table: dict[str, list[str]],
                           file_size_table: dict[str, int]):
    directory_size = 0
    for filepath in directory_files_table[directory_full_path]:
        filesize = file_size_table[filepath]
        if filesize == -1:
            filesize = compute_directory_size(filepath, directory_files_table,
                                              file_size_table)
        directory_size += filesize
    return directory_size


def find_directory_sizes(lines: list[str]):
    directory_files_table = {}
    file_size_table = {}
    directory_history = []
    current_dir = ""
    directory_size_table: dict[str, int] = {}
    for line in lines:
        current_dir = parse_line(line, directory_files_table, file_size_table,
                                 directory_history, current_dir)
    for directory in directory_files_table:
        if directory not in directory_size_table:
            directory_size_table[directory] = compute_directory_size(
                directory, directory_files_table, file_size_table)
    return directory_size_table


def find_total_size_of_directories_less_than_100000(directory_size_table):
    total_size = 0
    for directory in directory_size_table:
        if directory_size_table[directory] <= 100000:
            total_size += directory_size_table[directory]
    return total_size


def find_smallest_directory_to_delete(directory_size_table: list[str]):
    FILESYSTEM_MAX_CAPACITY = 70000000
    FREE_SPACE_REQUIRED = 30000000
    root_directory_size = directory_size_table["/"]
    free_space_left = FILESYSTEM_MAX_CAPACITY - root_directory_size
    space_to_free = FREE_SPACE_REQUIRED - free_space_left
    minimum_so_far = maxsize
    for directory in directory_size_table:
        if directory_size_table[directory] > space_to_free and \
        directory_size_table[directory] < minimum_so_far:
            minimum_so_far = directory_size_table[directory]
    return minimum_so_far


input_text = open("input.txt", "r", encoding="utf-8").read().split("\n")
directory_size_table = find_directory_sizes(input_text)
print(find_total_size_of_directories_less_than_100000(directory_size_table))
print(find_smallest_directory_to_delete(directory_size_table))
