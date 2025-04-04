"""This Code copies a text file from a specific location to the current working directory, then displaying both its content and its absolute path."""


expl=r"C:\Users\***\change_notice.txt"
with open (expl,'r') as readfile:
    with open ("change_notice2.txt",'w') as writefile:
        for line in readfile:
            writefile.write(line)

with open ("change_notice2.txt",'r') as readfile2:
    print((readfile2.read()))

import os


file_name = "change_notice2.txt"  
file_path = os.path.abspath(file_name)

print(f"The full path of {file_name} is:")
print(file_path)
