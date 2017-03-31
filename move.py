# move files from one directory to another
# if files alrady exist there, they will be overwritten
# retains original file date/time

import os,shutil

# make sure that these directories exist
dir_src = r"C:\Users\Spandan Majumder\Desktop\dest"
dir_dst = r"C:\Users\Spandan Majumder\Desktop\src" 
file_list=os.listdir(dir_src)
print("paths: ",file_list)
for file in file_list:
    print("Moved file name : ",file)  # testing
    src_file = os.path.join(dir_src, file)
    dst_file = os.path.join(dir_dst, file)
    shutil.move(src_file, dst_file)
