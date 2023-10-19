import os
from dotenv import load_dotenv
from github import Github, InputGitAuthor, MainClass

from authenitication_balancer import authentication_balancer

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO_NAME = "phoenicxai/start"

# Instantiate GitHub
g = Github(GITHUB_TOKEN)
user = g.get_user()

# Step 1: Create a new private repository
repo = user.create_repo(GITHUB_REPO_NAME, private=True)

# Step 2: Add essential files
file_list = [
    {"file_name": "README.md", "content": "# This is README"},
    {"file_name": "LICENSE", "content": "MIT License..."}, # Add full MIT License text here
    {"file_name": ".gitignore", "content": "node_modules/"}  # Sample content
]

author = InputGitAuthor("phoenicxai", "your_email@example.com")

for file in file_list:
    repo.create_file(file["file_name"], f"Add {file['file_name']}", file["content"], author=author)

# Step 3: Set up SSH Key and authenticate
try:
    authentication_balancer("path/to/local/repo", "git@github.com:phoenicxai/start.git")
except Exception as e:
    print(f"Error: {e}")
    # Step 4: Initiate debugger or handle the error as needed
    import pdb
    pdb.set_trace()  # Python's built-in debugger

print("All tasks completed!")
