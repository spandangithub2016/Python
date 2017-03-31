import os
dir_src = r"C:\Users\Spandan Majumder\Desktop\Desktop"
file_list=os.listdir(dir_src)
print("paths: ",file_list)

for file in file_list:
    # Split the extension from the path and convert it to lowercase.
    ext = os.path.splitext(file)[-1].lower()
    print(os.path.splitext(file))
    print(ext)
