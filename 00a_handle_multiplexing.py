# import required modules
import os

# SET PATHS
input_directory = "../input/01.RawData/"
required_extension = ".fq.gz"

print("handling multiplexing...")
# Function definitions
def group_files_by_common_postfix(file_names):
    grouped_files = {}
    
    for file_name in file_names:
        # Split the file name into parts based on underscores
        parts = file_name.split("_")
        
        # Check if the file name has at least one underscore
        if len(parts) > 1:
            # Use the last part as the common prefix for grouping
            common_postfix = parts[-1]
            
            # Add the file to the corresponding group
            if common_postfix in grouped_files:
                grouped_files[common_postfix].append(file_name)
            else:
                grouped_files[common_postfix] = [file_name]

    return grouped_files


# Get all the files in the input directory and make a list of their names
for root, dirs, files in os.walk(input_directory, topdown=False):
    # files in one folder with having requierd extension
    files_from_each_folder = []
    for name in files:
        file_with_path = os.path.join(root, name)
        if file_with_path.endswith(required_extension):
            files_from_each_folder.append(file_with_path)
    grouped_files = group_files_by_common_postfix(files_from_each_folder)
    
    # print("================================")


    # Print the grouped files
    for common_postfix, files in grouped_files.items():
        # print("********************************")
        # print("Common Postfix: {}".format(common_postfix))
        # print("Files: {}".format(', '.join(files)))
        # print()
        # if files are more than 2 then combine them
        if len(files) > 1:
            print("********************************")
            print("Combining files...")

            # add folder name to the combined file name
            folder_name = root.split("/")[-1]

            # combine the files using cat command
            combined_file_name = "{}_{}".format(folder_name, common_postfix)
            combined_file_path = os.path.join(root, combined_file_name)
            command = "cat {} > {}".format(' '.join(files), combined_file_path)
            print(command)
            os.system(command)
            print("Done combining files!")

            #remove the individual files
            print("Removing individual files...")
            for file in files:
                print("rm {}".format(file))
                os.remove(file)
            print("Done removing individual files!")
                