# GitHub Issues Creator

This script allows you to create GitHub issues in bulk from a CSV file. You can specify the organization, repository, personal access token, and CSV file path, either through command-line arguments or interactive prompts.

## Prerequisites

```python
requests library
```

## Installation

Clone the repository or download the script.

Install the required Python package:

```bash
pip install requests
```

## Usage

### Command-Line Arguments

You can run the script with the following command-line arguments:

`--org`: GitHub organization name
`--repo`: GitHub repository name
`--token`: GitHub personal access token
`--csv`: Path to the CSV file

Example:

```bash
python3 main.py --org Zenscalr --repo dataguard-web --token ghp_token --csv issues.csv
```

### Interactive Prompts

If you run the script without any arguments, it will prompt you to enter the required information interactively:

```bash
python3 main.py
```

## CSV Format

The CSV file should be formatted with the following headers:

`Task`: Main task description
`Sub-task`: Sub-task description
`Description`: Detailed description or user story

Example:

```csv
Task,Sub-task,Description
Persona Generator,Pull Name and Profile Picture,As an administrator, I want to retrieve user names and profile pictures from randomuser.me so that I can create realistic personas.
```

## Generating a Personal Access Token

You'll need a personal access token from GitHub to authenticate with the GitHub API. Follow these steps to create one:

- Go to Settings > Developer settings > Personal access tokens > Generate new token.
- Select the necessary permissions, including `repo` and `public_repo` if you're working with public repositories.
- Copy the generated token and use it as the `--token` argument or enter it at the interactive prompt.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. If you find any issues or have suggestions, please open an issue.
