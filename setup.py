import os
import subprocess
import sys
import venv


def create_venv(venv_dir="venv"):
    print("🔧 Creating virtual environment...")
    venv.create(venv_dir, with_pip=True)


def install_requirements(venv_dir="venv"):
    print("📦 Installing packages from requirements.txt...")

    if os.name == "nt":
        pip_path = os.path.join(venv_dir, "Scripts", "pip.exe")
    else:
        pip_path = os.path.join(venv_dir, "bin", "pip")

    subprocess.check_call([pip_path, "install", "-r", "requirements.txt"])


def main():
    create_venv()
    install_requirements()
    print("\n✅ Done!")
    if os.name == "nt":
        print("To activate the environment: venv\\Scripts\\activate")
    else:
        print("To activate the environment: source venv/bin/activate")


if __name__ == "__main__":
    main()
