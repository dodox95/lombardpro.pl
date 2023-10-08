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
    email = input("Podaj swój email: ")
    name = input("Podaj swoje imię: ")

    os.system(f"git config --{scope} user.email '{email}'")
    os.system(f"git config --{scope} user.name '{name}'")

def initialize_repo():
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'initial commit'")
    repo_link = input("Podaj link do repozytorium z GitHuba: ")
    os.system(f"git remote add origin {repo_link}")
    os.system("git push origin master")

def main():
    # Sprawdź czy folder jest repozytorium
    if not os.path.exists(".git"):
        choice = input("To nie jest repozytorium Git. Czy chcesz je zainicjować? (Tak/Nie) ").lower()
        if choice == 'tak':
            initialize_repo()
        else:
            return

    # Konfiguracja tożsamości
    scope_choice = input("Czy chcesz skonfigurować tożsamość dla bieżącego repozytorium czy globalnie? (bieżące/globalnie): ").lower()
    scope = '' if scope_choice == 'bieżące' else 'global'
    if not check_git_identity(scope):
        set_git_identity(scope)
    else:
        print(f"Tożsamość {scope_choice} została już skonfigurowana.")

    commit_message = input("Enter the update title: ")

    print("Fetching the latest changes from GitHub...")
    os.system("git pull")

    print("Adding all changes to the index...")
    os.system("git add .")

    print("Committing changes...")
    result = os.system(f'git commit -m "{commit_message}"')
    if result != 0:
        print("Commit nie powiódł się.")
        return

    print("Pushing changes to GitHub...")
    result = os.system("git push origin master")
    if result != 0:
        print("Push nie powiódł się.")
        return

    print("Update completed!")
    input("Press Enter to continue...")

if __name__ == "__main__":
    main()
