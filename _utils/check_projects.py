from pathlib import Path
import re

# Constants
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_DIR = BASE_DIR / "_projects"

def get_project_dirs()->list[Path]:
    """Return a list of all directories inside PROJECTS_DIR except those
    starting with an underscore."""
    return [
        path for path in PROJECTS_DIR.iterdir()
        if
        path.is_dir()
        and
        path.stem[0] != "_"
    ]

def check_authors_dot_text(dir):
    """Raise exception if dir does not contain authors.txt"""
    authors_file = dir/"authors.txt"
    if not authors_file.exists():
        raise FileNotFoundError(f"authors.txt missing from project folder {dir}")
    return authors_file

def check_index(dir):
    """Raise exception if:
    - dir does not contain index.md or index.html
    - [DISABLED] index does not contain front matter"""
    if (dir/"index.md").exists():
        index_file = dir/"index.md"
    elif (dir/"index.html").exists():
        index_file = dir/"index.html"
    else:
        raise FileNotFoundError(f"index missing from project folder {dir}")
    # with open(index_file,"r") as index:
    #     content = index.read()
    #     regex = "^---\n((.|\n)*|\n)---\n"  # Matches and captures front matter content
    #     front_matter = re.search(regex, content)
    #     if not front_matter:
    #         raise Exception(f"{index_file} missing front-matter")
    return index_file

def run_checks(dir):
    check_authors_dot_text(dir)
    check_index(dir)

if __name__=="__main__":
    project_dirs = get_project_dirs()
    for dir in project_dirs:
        run_checks(dir)