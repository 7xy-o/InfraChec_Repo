import re

def check_dockerfile_user(file_path):

    try:
        with open(file_path, "r") as file:
            content = file.read()
            pattern = r"^\s*USER\s+(?!root).+"
            match = re.search(pattern, content, re.MULTILINE | re.IGNORECASE)
            if match:
                return True, f"[pass] User defined: '{match.group().strip()}'"
            else:
                return False, f"[fail] No non-root USER instruction found. container might run as Root!"
    except FileNotFoundError:
        return False, f"[error] File not found: {file_path}"
