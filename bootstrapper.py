import os
import nbformat as nbf

def create_folder_structure(category, subcategory, utility_name):
    path = os.path.join("utils", category, subcategory, utility_name)
    os.makedirs(path, exist_ok=True)
    return path

def create_python_file(path):
    with open(os.path.join(path, "main.py"), "w") as file:
        file.write("# Python main file for the utility\n")
        file.write("def main():\n")
        file.write("    pass\n\n")
        file.write("if __name__ == '__main__':\n")
        file.write("    main()\n")

def create_javascript_file(path):
    with open(os.path.join(path, "index.js"), "w") as file:
        file.write("// JavaScript index file for the utility\n")
        file.write("function main() {\n")
        file.write("}\n\n")
        file.write("main();\n")

def create_jupyter_notebook(path, utility_name):
    nb = nbf.v4.new_notebook()

    # Title and Description
    nb.cells.append(nbf.v4.new_markdown_cell(f"# {utility_name}\n\nDescription of the utility goes here."))

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

def create_readme_file(path, utility_name):
    with open(os.path.join(path, "README.md"), "w") as file:
        file.write(f"# {utility_name}\n\n")
        file.write("Description of the utility goes here.\n\n")
        
        # Prerequisites Section
        file.write("## Prerequisites\n\n")
        file.write("List the prerequisites and dependencies here.\n\n")
        
        # Installation Section
        file.write("## Installation\n\n")
        file.write("Provide installation instructions here.\n\n")
        
        # Usage Section
        file.write("## Usage\n\n")
        file.write("### Command-Line Arguments\n\n")
        file.write("Describe any command-line arguments and provide examples.\n\n")
        
        # Interactive Prompts Section
        file.write("### Interactive Prompts\n\n")
        file.write("Explain how to use the utility interactively.\n\n")
        
        # Understanding the Utility Section
        file.write("## Understanding the Utility\n\n")
        file.write("Provide a detailed explanation of how the utility works, including any relevant formulas or concepts.\n\n")

def update_root_readme(category, subcategory, utility_name):
    readme_path = os.path.join("utils", "README.md")
    directory_path = f"{category}/{subcategory}/{utility_name}"

    with open(readme_path, "r") as file:
        lines = file.readlines()

    # Find the line index where the "Utilities" section ends
    insert_index = next((i for i, line in enumerate(lines) if "## How to Use" in line), None)

    # Insert the new utility's information
    if insert_index:
        lines.insert(insert_index, f"### {utility_name}\n\nLocated in the `{directory_path}` directory.\n\n- Directory: `{directory_path}`\n- Documentation: README\n\n")

    with open(readme_path, "w") as file:
        file.writelines(lines)


def main():
    print("Welcome to the Utility Bootstrapper!")
    category = input("Enter the category (e.g., physics, astrophysics): ")
    subcategory = input("Enter the subcategory (e.g., relativity, celestial_mechanics): ")
    utility_name = input("Enter the utility name: ")
    file_type = input("Enter the file type (python/js/jupyter): ")

    path = create_folder_structure(category, subcategory, utility_name)

    if file_type.lower() == "python":
        create_python_file(path)
    elif file_type.lower() == "js":
        create_javascript_file(path)
    elif file_type.lower() == "jupyter":
        create_jupyter_notebook(path, utility_name)

    create_readme_file(path, utility_name)

    update_root_readme(category, subcategory, utility_name)

    print(f"Utility '{utility_name}' has been successfully created!")

if __name__ == "__main__":
    main()
