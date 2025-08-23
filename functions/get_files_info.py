import os

from google.genai import types


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


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read content of specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to read content from, relative to the working directory.",
            ),
        },
    ),
)
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run python specified python file with provided arguments, constrained to the working directory and files ending in \".py\".",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="List of arguments to run the specified python file with.",
                items=types.Schema(type=types.Type.STRING),
                default=[]            )
        },
    ),
)
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to a file at the provided file path, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to write content to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file at the provided file path.",
            ),
        },
    ),
)
