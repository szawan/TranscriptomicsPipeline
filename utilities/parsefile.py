import os
import sys
import shutil
import subprocess
def parsefilename(dir_path, new_path):
    try:
        if not os.path.exists(dir_path):
            print(f"Directory path: {dir_path} doesnot exist.")
            return
        
        for file in os.listdir(dir_path):
            if file.endswith(".fastq.gz"):
                # file pattern cellline_treatment_Sample_L004_Rpair_001
                # print( file)
                li_path = file.split("_")
                cellline = li_path[0]
                treatment = li_path[1]
                Sample = li_path[2]
                pair = li_path[5]
                ext = li_path[6].replace('001',"")
                new_dir = cellline + "_" + treatment+"_"+Sample
                if not os.path.exists(os.path.join(new_path, new_dir)):
                    os.mkdir(os.path.join(new_path, new_dir))
                shutil.copy2(os.path.join(dir_path,file),os.path.join(new_path,new_dir))
                newfilename = new_dir+pair.replace("R","_")+ext
                print(newfilename)
                os.rename(os.path.join(new_path,new_dir+f"/{file}"), os.path.join(new_path,new_dir+f"/{newfilename}"))
                
    
    except Exception as ex:
        print(f"An error occurred: {ex}")

def parseDir(dir_path):

    try:
        if not os.path.exists(dir_path):
            print(f"Directory path: {dir_path} doesnot exist.")
            return
        
        for file in os.listdir(dir_path):
            if file.endswith(".fastq.gz"):
                filepath = os.path.join(dir_path, file)
                copy_command = f"cp {filepath} ./raw_data/"
                subprocess.call(copy_command,shell=True)


    except Exception as ex:
        print(f"An error occurred: {ex}")



if __name__ == "__main__":
    if len(sys.argv) !=3:
        print("Usage: python script.py /path/to/directory")
    
    else:
        directory_path = sys.argv[1]
        new_path = sys.argv[2]
        # parseDir(directory_path)
        parsefilename(directory_path, new_path)
