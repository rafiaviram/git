import os
import shutil

# function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# function to organize files based on their file types
def organize_files(source_folder):
    # list of file types to organize
    image_types = [".jpeg", ".jpg", ".png", ".gif"]
    video_types = [".avi", ".mp4", ".mov", ".mkv"]
    document_types = [".pdf", ".docx", ".xlsx", ".pptx"]

    # iterate over all files in the source folder
    for file_name in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file_name)

        # ignore directories
        if os.path.isdir(file_path):
            continue

        # determine the file type based on the file extension
        file_extension = os.path.splitext(file_name)[1].lower()
        if file_extension in image_types:
            destination_folder = os.path.join(source_folder, "Images")
        elif file_extension in video_types:
            destination_folder = os.path.join(source_folder, "Videos")
        elif file_extension in document_types:
            destination_folder = os.path.join(source_folder, "Documents")
        else:
            destination_folder = os.path.join(source_folder, "Other")

        # create the destination folder if it doesn't exist
        create_directory(destination_folder)

        # move the file to the destination folder
        shutil.move(file_path, destination_folder)

    print("Files have been organized successfully!")


# test the script
if __name__ == '__main__':
    source_folder = input("Enter the source folder path: ")
    organize_files(source_folder)
