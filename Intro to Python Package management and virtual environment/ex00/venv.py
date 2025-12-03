#!/usr/bin/env python3
import os

def get_env_path():
    env_path = os.environ.get('VIRTUAL_ENV')
    return env_path

def main():
    current = get_env_path()
    print(f'Your current virtual env is {current}')

if __name__ == '__main__':
    main()