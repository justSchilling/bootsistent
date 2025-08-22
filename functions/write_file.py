import os


def write_file(working_directory, file_path, content):
    abs_workdir = os.path.abspath(working_directory)
    abs_file = os.path.abspath(os.path.join(abs_workdir, file_path))
    if not abs_file.startswith(abs_workdir):
        return (
            f'Error: Cannot write to "{file_path}" as it is outside the permitted '
            + "working directory"
        )

    with open(abs_file, "w") as file:
        file.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
