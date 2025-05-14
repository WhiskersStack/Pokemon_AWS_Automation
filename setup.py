import os
import subprocess
import sys
import venv
import subprocess


def create_venv(venv_dir="venv"):
    print("Creating virtual environment...")
    venv.create(venv_dir, with_pip=True)


def install_requirements(venv_dir="venv"):
    print("Installing packages from requirements.txt...")
    pip_path = os.path.join(venv_dir, "Scripts" if os.name == "nt" else "bin", "pip")
    subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])


def run_main_script():
    subprocess.check_call([sys.executable, "main.py"])


def main():
    create_venv()
    install_requirements()
    run_main_script()
    print("\n✅ All done!")


if __name__ == "__main__":
    main()
