# Utils

A collection of handy utilities and scripts that can be used to automate various tasks, enhance workflows, and more. This repository is intended to be a growing compilation of useful tools that can be leveraged by developers, administrators, and anyone who finds them beneficial.

## Utilities

### GitHub Issue Creator

Located in the `github/issue_creator` directory, this utility allows you to create GitHub issues in bulk from a CSV file. It's perfect for project managers and developers who want to automate the process of adding issues to GitHub repositories.

- Directory: `github/issue_creator`
- Documentation: README

### Heat Transfer

The heat_transfer utility provides tools for calculating and analyzing heat transfer in various materials and conditions. Utilizing common heat transfer models such as conduction, convection, and radiation, this utility can be applied to engineering, physics, and environmental studies. Whether you're designing a thermal system, studying climate effects, or exploring material properties, the heat_transfer utility offers a flexible and efficient solution.

- Directory: `./physics/thermodynamics/heat_transfer`
- Documentation: README

## How to Use

Each utility in this repository comes with its own README file that provides detailed instructions on how to use it. Navigate to the specific utility's directory to find its README and any other relevant files.

## Contributing

Contributions are welcome! If you have a utility or script that you think would be a valuable addition to this repository, please feel free to fork the repository and submit a pull request. If you find any issues or have suggestions for improvements, please open an issue.

## Adding a New Utility

To add a new utility, you can use the utility bootstrapper script located in the root directory. Follow these steps:

1. Run the bootstrapper script: 
    - If you don't have Python installed, you can download it [here](https://www.python.org/downloads/).
    - Activate the virtual environment by running `source venv/bin/activate` from the root directory.
    - Install the required packages by running `pip install -r requirements.txt` from the root directory.
    - Run the bootstrap utility by running `python bootstrapper.py` from the root directory.
2. Follow the interactive prompts to specify the category, subcategory, utility name, and file type (Python, JavaScript, or Jupyter notebook).
3. The script will create the appropriate folder structure, main file (e.g., main.py, index.js, or Jupyter notebook), and a README.md file for the utility.
4. Customize the generated files as needed, and add a brief description of the utility to the main README file, along with a link to the utility's directory and README.

### Example

```bash
python3 bootstrapper.py \ 
--category physics \ 
--subcategory thermodynamics \ 
--utility_name heat_transfer \ 
--description "The heat_transfer utility provides tools for calculating and analyzing heat transfer in various materials and conditions. Utilizing common heat transfer models such as conduction, convection, and radiation, this utility can be applied to engineering, physics, and environmental studies. Whether you're designing a thermal system, studying climate effects, or exploring material properties, the heat_transfer utility offers a flexible and efficient solution." \ 
--file_types python,jupyter
```

Alternatively, you can manually create a new directory for the utility within the appropriate category (e.g., github), include a README file in the utility's directory with detailed instructions on how to use it, and update the main README file as described above.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Future Plans

I plan to continuously expand this repository with more utilities that cater to various needs. Stay tuned for updates, and feel free to suggest or contribute new tools!
