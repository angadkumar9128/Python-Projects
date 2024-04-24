import zipfile
import os
import shutil

def extract_zip(zip_file_path):
    """
    Extracts a zip file to a folder with the same name in the same directory.

    Args:
        zip_file_path (str): Path to the zip file.
    """
    # Check if the zip file exists
    if not os.path.exists(zip_file_path):
        print(f"Error: The zip file '{zip_file_path}' does not exist.")
        return

    # Get the directory and filename from the zip file path
    directory, filename = os.path.split(zip_file_path)

    # Remove the ".zip" extension from the filename to get the folder name
    folder_name = os.path.splitext(filename)[0]

    # Create the destination folder if it doesn't exist
    destination_folder = os.path.join(directory, folder_name)
    os.makedirs(destination_folder, exist_ok=True)

    try:
        # Open the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Extract all files and directories from the zip file
            zip_ref.extractall(destination_folder)
        print("Extraction successful!")
    except zipfile.BadZipFile:
        print("Error: The specified file is not a valid zip file.")
    except Exception as e:
        print(f"Error: {e}")

def create_zip(source_path):
    """
    Creates a zip file containing either a single folder or multiple files.

    Args:
        source_path (str): Path to the folder or file to be zipped.
    """
    # Check if the source path exists
    if not os.path.exists(source_path):
        print(f"Error: The source path '{source_path}' does not exist.")
        return

    # Check if the source path is a folder or a file
    if os.path.isdir(source_path):
        # Create a zip file containing the entire folder
        try:
            shutil.make_archive(source_path, 'zip', source_path)
            print(f"Zip creation successful! Zip file saved as '{source_path}.zip'")
        except Exception as e:
            print(f"Error: {e}")
    elif os.path.isfile(source_path):
        # Create a zip file containing the single file
        try:
            destination_folder = os.path.dirname(source_path)
            with zipfile.ZipFile(f"{source_path}.zip", 'w') as zip_ref:
                zip_ref.write(source_path, os.path.basename(source_path))
            print(f"Zip creation successful! Zip file saved as '{source_path}.zip'")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Error: '{source_path}' is neither a folder nor a file.")

def main():
    while True:
        print("Select an option:")
        print("1. Zip a folder or file")
        print("2. Extract a zip file")
        print("3. Exit")
        choice = input("Enter 1, 2, or 3: ")

        if choice == '1':
            source_path = input("Enter the path to the folder or file you want to zip: ")
            create_zip(source_path)
        elif choice == '2':
            zip_file_path = input("Enter the path to unzip the file: ")
            extract_zip(zip_file_path)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
