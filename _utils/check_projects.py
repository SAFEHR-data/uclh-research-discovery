from pathlib import Path
import re

from yaml import load, Loader


# Constants
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_DIR = BASE_DIR / "_projects"
STATUS_LIST = ["ongoing","completed"]  # First value is default
FRONT_MATTER_REQS = {
    "layout": ["project"],
    "title": None,
    "status": STATUS_LIST,
    "authors": None
}
TABS_REQS = {
    "name": None,
    "type": ["md","html"],
    "source": None,
    "label": None
}

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

def check_tabs(fm_yaml, index_file):
    """For each tab item check format and confirm source exists"""
    tabs = fm_yaml.get("tabs")
    for tab in tabs:
        for param, value_list in TABS_REQS.items():
            value = tab.get(param)
            if not value:
                raise ValueError(f"Misconfigured tab data in {index_file}, missing {param}.")
            if value_list and value not in value_list:
                raise ValueError(f"Unrecognised value for tab:{param} in {index_file}: {value}.")
        source = tab.get("source")
        if not (index_file.parent / source).exists():
            raise FileNotFoundError(f"Source file {source} referenced in {index_file} not found.")

def check_front_matter(fm_text, index_file):
    """Check front matter content conforms to required values"""
    fm_yaml = load(fm_text, Loader=Loader)
    for param, value_list in FRONT_MATTER_REQS.items():
        value = fm_yaml.get(param)
        if not value:
            raise ValueError(f"{index_file} front matter does not contain {param}")
        if value_list:  # If None, accept any value
            if value not in value_list:
                raise ValueError(f"{index_file} front matter contains illegal value for {param}: {value}")
    check_tabs(fm_yaml, index_file)

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
    #     check_front_matter(front_matter.groups(0)[0], index_file)
    return index_file

def run_checks(dir):
    check_index(dir)

if __name__=="__main__":
    project_dirs = get_project_dirs()
    for dir in project_dirs:
        run_checks(dir)