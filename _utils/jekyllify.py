"""
Takes a project folder containing a set of plain markdown files and makes it
Jekyll ready by adding front matter and inferring page variables from the
contents.

As a minimum the project folder should contain:
- index.md: The project landing page featuring a lay summary
- authors.txt: A list of authors to be credited for the project (one per line)

## Additional content
Each other markdown file in the folder will be included as an additional tab
on the landing page. The tab label will be the filename in title case.
"""

import argparse
from pathlib import Path
import random
import re
from string import ascii_lowercase
from titlecase import titlecase


# Constants
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECTS_DIR = BASE_DIR / "_projects"


argument_parser = argparse.ArgumentParser(
    prog="Jekyllifier",
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

project_arg_help = """Name of the project folder to process. If this is omitted
all project folders that don't contain yaml front matter at the top of index.md
will be processed."""

argument_parser.add_argument(
    "-p","--project", help=project_arg_help, default=None
)

def can_process_dir(dir:Path, raise_exception:bool=False) -> bool:
    """Given a directory path, check the content meets the minimum
    requirements, and that it has not previously been jekyllified."""
    # Is there a file called index.md?
    try:
        with open(dir / "index.md","r") as index:
            # If index.md already has front matter it should not be processed
            content = index.read()
            regex = "^---\n((.|\n)*|\n)---\n"  # Matches and captures front matter content
            front_matter = re.search(regex, content)
            if front_matter:
                return False
    except FileNotFoundError:
        if raise_exception:
            raise FileNotFoundError(f"index.md missing from project folder {dir}")
        return False
    # Is there a file called authors.txt?
    try:
        with open(dir / "authors.txt","r") as index:
            pass
    except FileNotFoundError:
        if raise_exception:
            raise FileNotFoundError(f"authors.txt missing from project folder {dir}")
        return False
    return True

def get_project_dirs(name:str=None)->list[Path]:
    """Either return the path to the named project folder inside a list or, if no
    name is provided, return a list of all directories inside PROJECTS_DIR."""
    if name:
        project_dir = PROJECTS_DIR / name
        if project_dir.exists():
            return [project_dir]
        else:
            raise FileNotFoundError(f"No directory named {name} found under {PROJECTS_DIR}")
    else:
        return [
            path for path in PROJECTS_DIR.iterdir()
            if
              path.is_dir()
            and
              path.stem[0] != "_"
            ]

def get_random_string(len:int) -> str:
    return ''.join(random.choice(ascii_lowercase) for i in range(len))

def get_tab_source_files(dir:Path) -> list[Path]:
    source_files = list(dir.glob("*.md")) + list(dir.glob("*.html"))
    # Remove index.md or index.html
    for index in [dir/"index.md", dir/"index.html"]:
        if index in source_files:
            source_files.remove(index)
    return source_files

def generate_label_from_filename(stem:str) -> str:
    """Given a filename stem (e.g. 03_code-and_data) convert this to a label by:

    1. replacing any - or _ characters with spaces
    2. removing any whitespace remaining at the start or end of the name
    3. removing any digits at the start of the filename
    4. converting the name to title case"""
    label = stem.replace("_"," ").replace("-"," ")
    label = label.strip()
    label = re.sub("^[\d]*","",label)
    return titlecase(label)

def generate_title_yaml(dir:Path) -> str:
    """Title can come from title.txt, or the project folder name will be used.
    If using the folder name, underscores and dashes are replaced with space
    and then converted to title case."""
    title=""
    if (dir/"title.txt").exists():
        with open(dir/"title.txt","r") as f:
            title = f.read()
    if not title:
        title = generate_label_from_filename(dir.name)
    return f"title: {title}\n"

def generate_authors_yaml(dir:Path) -> str:
    """Create yaml block style list of authors, where each author appears
    on a separate line in authors.txt"""
    authors = "authors:\n"
    with open(dir / "authors.txt", "r") as f:
        for author in f.readlines():
            author = author.strip()  # remove any whitespace/newlines either side
            if author:  # ignores blank lines
                authors += f"- {author}\n"
    return authors

def generate_tabs_yaml(dir:Path) -> str:
    """Search the given directory for extra .md or .html files (other than index.md/
    index.html) and return a yaml block style list of tabs referencing those files.
    Attributes type, source, and label are generated from the file name, and name is
    a randomly generated string."""
    source_files = get_tab_source_files(dir)
    tabs = "tabs:\n"
    for file in source_files:
        tabs += "- {\n"
        tabs += f"  name: {get_random_string(8)},\n"  # Used as html element id
        tabs += f"  type: {file.suffix[1:]},\n"  # Remove the dot from suffix
        tabs += f"  source: {file.name},\n"
        tabs += f"  label: {generate_label_from_filename(file.stem)}\n"
        tabs += "  }\n"
    return tabs

def prepend_underscores_to_tab_sources(dir:Path)-> None:
    """For each file in the directory with a .html or .md suffix, rename and prepend
    with an underscore character (except for index.md)"""
    source_files = get_tab_source_files(dir)
    for file in source_files:
        if not file.stem[0] == "_":
            file.rename(file.with_stem("_"+file.stem))

def jekyllify(dir:Path)->None:
    """Given a project directory, add underscores to any .md or .html files other than
    index.md to ensure they do not get processed by Jekyll, then generate yaml front
    matter and prepend to index.md."""
    print(f"Jekyllifying {dir}")
    prepend_underscores_to_tab_sources(dir)
    front_matter = "---\n"
    front_matter += "layout: project\n"  # layout is always project
    front_matter += generate_title_yaml(dir)
    front_matter += generate_authors_yaml(dir)
    front_matter += generate_tabs_yaml(dir)
    front_matter += "---\n\n"
    with open(dir/"index.md","r+") as f:
        content = f.read()
        f.seek(0,0)
        f.write(front_matter + content)

if __name__=="__main__":
    print("Jekyllify script running...")
    args = argument_parser.parse_args()
    if args.project:
        dirs_to_jekyllify = [
            dir for dir in get_project_dirs(args.project)
            if can_process_dir(dir, raise_exception=True)
        ]
    else:
        dirs_to_jekyllify = [dir for dir in get_project_dirs() if can_process_dir(dir)]
    for dir in dirs_to_jekyllify:
        jekyllify(dir)
    print("Jekyllify script completed")
