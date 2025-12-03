#!/usr/bin/env python3
import os
import sys
import subprocess
import tempfile


def check_correct_env():
    if not (hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)):
        raise EnvironmentError("The script must be run in a virtual environment.")


def install_libraries():
    requirements_content = "beautifulsoup4>=4.9.0\npytest>=6.0.0\n"

    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        f.write(requirements_content)
        temp_req_file = f.name

    try:
        subprocess.run([
            sys.executable, '-m', 'pip', 'install', '-r', temp_req_file
        ], capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Installation error: {e}")
        raise
    finally:
        os.unlink(temp_req_file)


def get_installed_packages():
    result = subprocess.run([
        sys.executable, '-m', 'pip', 'list', '--format=freeze'
    ], capture_output=True, text=True, check=True)

    packages = []
    for line in result.stdout.strip().split('\n'):
        if line.strip() and '==' in line:
            packages.append(line.strip())

    return sorted(packages)


def save_requirements(packages):
    with open('requirements.txt', 'w') as f:
        for package in packages:
            f.write(package + '\n')


def main():
    check_correct_env()
    install_libraries()

    packages = get_installed_packages()

    print("Installed packages:")
    for package in packages:
        print(package)

    save_requirements(packages)


if __name__ == "__main__":
    main()