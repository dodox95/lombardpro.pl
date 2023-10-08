import os

def check_git_identity(scope='global'):
    email_config = f"git config --{scope} user.email"
    name_config = f"git config --{scope} user.name"
    
    email = os.popen(email_config).read().strip()
    name = os.popen(name_config).read().strip()

    if email and name:
        return True
    return False

def set_git_identity(scope='global'):
    email = input("Enter your email: ")
    name = input("Enter your name: ")

    os.system(f"git config --{scope} user.email '{email}'")
    os.system(f"git config --{scope} user.name '{name}'")

def initialize_repo():
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'initial commit'")
    repo_link = input("Enter the link to your GitHub repository: ")
    os.system(f"git remote add origin {repo_link}")
    os.system("git push origin master")

def main():
    # Check if the directory is a git repository
    if not os.path.exists(".git"):
        choice = input("This is not a Git repository. Do you want to initialize it? (Yes/No) ").lower()
        if choice == 'yes':
            initialize_repo()
        else:
            return

    # Identity configuration
    print("Do you want to configure identity for the current repository or globally?")
    scope_choice = input("1. Global\n2. Local\nChoice: ")
    scope = '' if scope_choice == '2' else 'global'
    if not check_git_identity(scope):
        set_git_identity(scope)
    else:
        print(f"The {scope} identity is already configured.")

    commit_message = input("Enter the update title: ")

    print("Fetching the latest changes from GitHub...")
    os.system("git pull")

    print("Adding all changes to the index...")
    os.system("git add .")

    print("Committing changes...")
    result = os.system(f'git commit -m "{commit_message}"')
    if result != 0:
        print("Commit failed.")
        return

    print("Pushing changes to GitHub...")
    result = os.system("git push origin master")
    if result != 0:
        print("Push failed.")
        return

    print("Update completed!")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()
