#!/usr/bin/python3
import os

def check_env_file():
    if not os.path.exists('.env'):
        print("\nError: \nStep1: Copy the env.example to .env and set all the notset fields.\n")
        return False
    return True

def check_env_fields():
    with open('.env', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if 'notset' in line:
                return False
    return True

def main():
    # Check that there exists a .env file.
    if not check_env_file():
        return

    # Check that all the fields are set in the .env file.
    if not check_env_fields():
        print("Some fields in .env are not set. Please set all fields.")
    else:
        print("All fields in .env are properly set.")

if __name__ == "__main__":
    main()

