import os,shutil

dir_src = r"C:\Users\Spandan Majumder\Desktop\work folder\src"
file_list=os.listdir(dir_src)
print("paths: ",file_list)

for file in file_list:
    # Split the extension from the path and convert it to lowercase.
    ext = os.path.splitext(file)[-1].lower()
    print(ext)
    # Now we can simply use == to check for equality, no need for wildcards.
    
    if ext.endswith(('.mp3')):
        src_file = os.path.join(dir_src, file)
        dst_file = os.path.join(r"C:\Users\Spandan Majumder\Desktop\work folder\mp3", file)
        
    elif ext.endswith(('.png', '.jpg', '.jpeg')):
        src_file = os.path.join(dir_src, file)
        dst_file = os.path.join(r"C:\Users\Spandan Majumder\Desktop\work folder\pics", file)
        
    elif ext.endswith(('.pdf','.txt','.ppt','.doc','.pps','.exe')):
        src_file = os.path.join(dir_src, file)
        dst_file = os.path.join(r"C:\Users\Spandan Majumder\Desktop\work folder\pdf", file)
        
    else:
        src_file = os.path.join(dir_src, file)
        dst_file = os.path.join(r"C:\Users\Spandan Majumder\Desktop\work folder\mixed", file)
    #common to all
    shutil.move(src_file,dst_file)
