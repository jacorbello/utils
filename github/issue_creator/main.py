import requests
import csv
import argparse

def create_issues(org, repo, token, csv_path):
    # Set up the headers with the provided GitHub token
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json',
    }

    # Construct the URL for the specified organization and repository
    url = f'https://api.github.com/repos/{org}/{repo}/issues'

    # Read the CSV file with the specified encoding
    with open(csv_path, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Prepare the issue data from the CSV row
            issue = {
                'title': f"{row['Task']} - {row['Sub-task']}",
                'body': row['Description'],
            }

            # Make the POST request to create the issue
            response = requests.post(url, json=issue, headers=headers)
            if response.status_code == 201:
                print(f"Issue created: {row['Task']} - {row['Sub-task']}: {response.json()['html_url']}")
            else:
                print(f"Failed to create issue: {response.content}")

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description='Create GitHub issues from a CSV file.')
    parser.add_argument('--org', help='GitHub organization name')
    parser.add_argument('--repo', help='GitHub repository name')
    parser.add_argument('--token', help='GitHub personal access token')
    parser.add_argument('--csv', help='Path to the CSV file')

    args = parser.parse_args()

    # Prompt the user for any missing arguments
    org = args.org or input('Enter the GitHub organization name: ')
    repo = args.repo or input('Enter the GitHub repository name: ')
    token = args.token or input('Enter your GitHub personal access token: ')
    csv_path = args.csv or input('Enter the path to the CSV file: ')

    # Call the function to create the issues
    create_issues(org, repo, token, csv_path)
