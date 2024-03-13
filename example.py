# Write a simplest python script that would show the content of the directory using the system library, where the path is specified by the user input. 

# from os import system
# system("ls " + input())

import os

def list_directory_contents():
    try:
        # Get the directory path from user input
        input_directory = input("Please type in the full path of the folder containing your files: ")

        # List all files and subdirectories in the specified directory
        contents = os.listdir(input_directory)

        if contents:
            print("Contents of the specified directory:")
            for item in contents:
                print(item)
        else:
            print("The specified directory is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
list_directory_contents()
