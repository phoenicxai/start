from github import Github

from git_athentication import GIT_STATE_NEGATIVE, GIT_STATE_NEUTRAL, GIT_STATE_POSITIVE, SSH_KEYS, git_balancer, set_ssh_key_for_state

# Your GitHub token to access the API
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO_NAME = "phoenicxai/start"

def authentication_balancer(path, remote_url):
    # 1. Ensure each state has a corresponding SSH private key
    for state, ssh_key in SSH_KEYS.items():
        if not os.path.exists(ssh_key):
            raise ValueError(f"SSH key for state {state} not found at {ssh_key}")

    # 2. Set SSH key for the current state (for demonstration)
    set_ssh_key_for_state(GIT_STATE_POSITIVE)

    # 3 & 4. Use GitHub API to verify SSH key presence
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(GITHUB_REPO_NAME)
    keys = [key.title for key in repo.get_keys()]
    
    for state in [GIT_STATE_POSITIVE, GIT_STATE_NEGATIVE, GIT_STATE_NEUTRAL]:
        key_name = f"Key for {state}"
        if key_name not in keys:
            raise ValueError(f"SSH public key for state {state} not added to GitHub repository")

    # 5. If everything is confirmed, execute the git_balancer
    return git_balancer(path, remote_url)

# Key things to note
# ... (your provided notes)

# Execute the function
path = "/Users/thusithadissanayake/start"
remote_url = "https://github.com/phoenicxai/start.git"
print(authentication_balancer(path, remote_url))