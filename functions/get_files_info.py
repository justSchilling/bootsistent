import os


def get_files_info(working_directory, directory="."):
    abs_workdir = os.path.abspath(working_directory)
    abs_dir = os.path.abspath(os.path.join(abs_workdir, directory))
    if not abs_dir.startswith(abs_workdir):
        return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
    if not os.path.isdir(abs_dir):
        return f"Error \"{directory}\" is not a directory"

    contents = os.listdir(abs_dir)
    content_infos = []
    for c in contents:
        c_path = os.path.join(abs_dir, c)      
        content_infos.append(f"- {c}: file_size={os.path.getsize(c_path)} bytes,"
            + f" is_dir={os.path.isdir(c_path)}")

    return "\n".join(content_infos)
