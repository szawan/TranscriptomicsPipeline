# import required modules
import os

# SET PATHS
input_directory = "../input/01.RawData/"
file_name_extras = "" # i.e. "clean" if it is not present then leave it blank
required_extension = ".fq.gz"

print("renaming files...")

# rename files in a folder based on folder name
for root, dirs, files in os.walk(input_directory, topdown=False):
    # files in one folder with having requierd extension
    files_from_each_folder = []
    for name in files:
        file_with_path = os.path.join(root, name)
        # folder name
        folder_name = root.split("/")[-1]
        # if file ends with _1 and required extension then rename it
        if file_with_path.endswith("_1" + file_name_extras + required_extension):
            print(name)
            # rename file
            os.rename(file_with_path, os.path.join(root, folder_name+"_1"+required_extension))
        # if file ends with _2 and required extension then rename it
        elif file_with_path.endswith("_2" + file_name_extras + required_extension):
            print(name)
            # rename file
            os.rename(file_with_path, os.path.join(root, folder_name+"_2"+required_extension))