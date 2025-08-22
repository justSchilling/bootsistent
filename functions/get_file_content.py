import os


MAX_CHARS = 10000

def get_file_content(working_directory, file_path):
    abs_workdir = os.path.abspath(working_directory)
    abs_file = os.path.abspath(os.path.join(abs_workdir, file_path))
    if not abs_file.startswith(abs_workdir):
        return (
            f'Error: Cannot read"{file_path}" as it is outside the permitted '
            + "working directory"
        )
    if not os.path.isfile(abs_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    with open(abs_file, "r") as file:
        return file.read(MAX_CHARS)
