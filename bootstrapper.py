import os
import nbformat as nbf
import argparse
import re
import git

def is_valid_name(name):
    return bool(re.match("^[a-zA-Z0-9_]+$", name))

def create_new_branch(branch_name):
    repo = git.Repo(".")
    new_branch = repo.create_head(branch_name)
    new_branch.checkout()

def commit_changes(commit_message):
    repo = git.Repo(".")
    repo.git.add(A=True)
    repo.index.commit(commit_message)

def create_folder_structure(category, subcategory, utility_name):
    path = os.path.join(".", category, subcategory, utility_name)
    os.makedirs(path, exist_ok=True)
    return path

def create_python_file(path):
    with open(os.path.join(path, "main.py"), "w") as file:
        file.write(PYTHON_TEMPLATE)

def create_javascript_file(path):
    with open(os.path.join(path, "index.js"), "w") as file:
        file.write(JS_TEMPLATE)

def create_jupyter_notebook(path, utility_name, description):
    nb = nbf.v4.new_notebook()

    # Title and Description
    nb.cells.append(nbf.v4.new_markdown_cell(f"# {capitalize_utility_name(utility_name)}\n\n{description}"))

    # Prerequisites Section
    nb.cells.append(nbf.v4.new_markdown_cell("## Prerequisites\n\nList the prerequisites and dependencies here."))

    # Installation Section
    nb.cells.append(nbf.v4.new_markdown_cell("## Installation\n\nProvide installation instructions here."))

    # Usage Section
    nb.cells.append(nbf.v4.new_markdown_cell("## Usage\n\nDescribe how to use the utility, including examples."))

    # Understanding the Utility Section
    nb.cells.append(nbf.v4.new_markdown_cell("## Understanding the Utility\n\nProvide a detailed explanation of how the utility works."))

    with open(os.path.join(path, f"{utility_name}.ipynb"), "w") as file:
        nbf.write(nb, file)

def create_readme_file(path, utility_name, description):
    print("Creating README.md file...")
    content = README_TEMPLATE.format(utility_name=utility_name, description=description)
    with open(os.path.join(path, "README.md"), "w") as file:
        file.write(content)


def update_root_readme(directory_path, utility_name, description):
    readme_path = os.path.join(".", "README.md")

    with open(readme_path, "r") as file:
        lines = file.readlines()

    # Find the line index where the "Utilities" section ends
    insert_index = next((i for i, line in enumerate(lines) if "## How to Use" in line), None)

    # Insert the new utility's information
    if insert_index:
        lines.insert(insert_index, f"### {utility_name}\n\n{description}\n\n- Directory: `{directory_path}`\n- Documentation: README\n\n")

    with open(readme_path, "w") as file:
        file.writelines(lines)

def capitalize_utility_name(utility_name):
    return ' '.join(word.capitalize() for word in utility_name.split('_'))


def main():
    parser = argparse.ArgumentParser(description="Utility Bootstrapper")
    parser.add_argument("--category", type=str, help="The category of the utility (e.g., physics, astrophysics)")
    parser.add_argument("--subcategory", type=str, help="The subcategory of the utility (e.g., relativity, celestial_mechanics)")
    parser.add_argument("--utility_name", type=str, help="The name of the utility")
    parser.add_argument("--description", type=str, help="A brief description of the utility")
    parser.add_argument("--file_types", type=str, help="Comma-separated list of file types (python/js/jupyter)")

    args = parser.parse_args()

    print("Welcome to the Utility Bootstrapper!")
    category = args.category if args.category else input("Enter the category (e.g., physics, astrophysics): ")
    if not is_valid_name(category):
        print("Invalid category name. Please use only alphanumeric characters and underscores.")
        return
    subcategory = args.subcategory if args.subcategory else input("Enter the subcategory (e.g., relativity, celestial_mechanics): ")
    if not is_valid_name(subcategory):
        print("Invalid subcategory name. Please use only alphanumeric characters and underscores.")
        return
    utility_name = args.utility_name if args.utility_name else input("Enter the utility name: ")
    if not is_valid_name(utility_name):
        print("Invalid utility name. Please use only alphanumeric characters and underscores.")
        return
    capitalized_utility_name = capitalize_utility_name(utility_name)    
    description = args.description if args.description else input("Enter a brief description of the utility: ")
    if not description:
        print("Description cannot be empty.")
        return
    file_types = args.file_types.split(",") if args.file_types else input("Enter the file types (comma-separated, e.g., python,js,jupyter): ").split(",")

    branch_name = f"add-{utility_name}-utility"
    print(f"Creating a new branch '{branch_name}'...")
    create_new_branch(branch_name)

    print(f"Creating the '{category}/{subcategory}/{utility_name}' directory structure...")
    path = create_folder_structure(category, subcategory, utility_name)

    for file_type in file_types:
        if file_type.lower().strip() == "python":
            print("Creating Python file...")
            create_python_file(path)
        elif file_type.lower().strip() == "js":
            print("Creating JavaScript file...")
            create_javascript_file(path)
        elif file_type.lower().strip() == "jupyter":
            print("Creating Jupyter notebook...")
            create_jupyter_notebook(path, utility_name, description)


    create_readme_file(path, capitalized_utility_name, description)

    update_root_readme(path, capitalized_utility_name, description)

    commit_message = f"Add {utility_name} utility"
    commit_changes(commit_message)

    print(f"Pushing changes to remote branch '{branch_name}'...")

    print(f"Utility '{capitalized_utility_name}' has been successfully created in the '{category}/{subcategory}/{utility_name}' directory.")

PYTHON_TEMPLATE = """\
# Python main file for the utility
def main():
    pass

if __name__ == '__main__':
    main()
"""

JS_TEMPLATE = """\
// JavaScript index file for the utility
function main() {
}

main();
"""

README_TEMPLATE = """\
# {utility_name}

{description}

## Prerequisites

List the prerequisites and dependencies here.

## Installation

Provide installation instructions here.

## Usage

### Command-Line Arguments

Describe any command-line arguments and provide examples.

### Interactive Prompts

Explain how to use the utility interactively.

## Understanding the Utility

Provide a detailed explanation of how the utility works, including any relevant formulas or concepts.
"""


if __name__ == "__main__":
    main()
