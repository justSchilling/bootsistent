import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    abs_workdir = os.path.abspath(working_directory)
    abs_file = os.path.abspath(os.path.join(abs_workdir, file_path))
    if not abs_file.startswith(abs_workdir):
        return (
            f'Error: Cannot execute "{file_path}" as it is outside the permitted '
            + "working directory"
        )

    if not os.path.isfile(abs_file):
        return f'Error: File "{file_path}" not found.'

    if not abs_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(
            args=["python", abs_file, *args],
            capture_output=True,
            cwd=working_directory,
            timeout=30,
        )
    except Exception as e:
        return f"Error: executing Python file: {e}"

    result = []
    if len(completed_process.stdout) > 0:
        result.append(f"STDOUT: {completed_process.stdout}")
    if len(completed_process.stderr) > 0:
        result.append(f"STDERR: {completed_process.stderr}")
    if len(result) == 0:
        result.append("No output produced")

    return "\n".join(result)
