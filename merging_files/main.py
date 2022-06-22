import os


def merge_files(directory: str, file_names: list, write_file: str) -> None:
    records_list = list()

    for file_name in file_names:
        with open(os.path.join(directory, file_name), encoding='utf-8') as file:
            file_lines = file.readlines()
            records_list.append([
                file_name + '\n',
                str(len(file_lines)) + '\n'
            ] + file_lines + ['\n'])

    records_list.sort(key=lambda x: x[1])

    with open(write_file, 'w', encoding='utf-8') as file:
        for records in records_list:
            file.writelines(records)


if __name__ == '__main__':
    merge_files(
        'files',
        [
            '1.txt',
            '2.txt',
            '3.txt'
        ],
        'new_file.txt'
    )
