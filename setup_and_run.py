import os
import subprocess
import sys

def run_command(command, check=True):
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, check=check, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Error running command: {result.stderr.decode('utf-8')}")
    else:
        print(result.stdout.decode('utf-8'))

def install_pyenv():
    if not subprocess.run("command -v pyenv", shell=True, stdout=subprocess.PIPE).stdout:
        print("pyenv not found. Installing pyenv...")
        run_command("curl https://pyenv.run | bash")
        
        # Add pyenv to PATH and initialize it
        home = os.path.expanduser("~")
        bashrc = os.path.join(home, ".bashrc")
        with open(bashrc, "a") as f:
            f.write('\nexport PATH="$HOME/.pyenv/bin:$PATH"\neval "$(pyenv init --path)"\neval "$(pyenv init -)"\neval "$(pyenv virtualenv-init -)"\n')
        print("pyenv installed. Please restart your terminal or run 'source ~/.bashrc'")
        sys.exit(0)  # Exit to restart the terminal for pyenv to be available
    else:
        print("pyenv is already installed.")

def install_python_version(version="3.10.9"):
    run_command(f"pyenv install -s {version}")

def create_virtualenv(name="vicky", python_version="3.10.9"):
    run_command(f"pyenv virtualenv {python_version} {name}")

def activate_virtualenv(name="vicky"):
    run_command(f"pyenv activate {name}")

def install_requirements():
    if os.path.isfile("requirements.txt"):
        run_command("pip install -r requirements.txt")
    else:
        print("requirements.txt not found. Please make sure it exists in the current directory.")
        sys.exit(1)

def run_django_server():
    run_command("python manage.py runserver")

def main():
    install_pyenv()
    install_python_version()
    create_virtualenv()
    activate_virtualenv()
    install_requirements()
    run_django_server()

if __name__ == "__main__":
    main()
