import os
import string
def rename_files():
    file_list=os.listdir(r"C:\Users\I326017\Downloads\prank\prank")
    print file_list
    print "present working directory ",os.getcwd(),"\n"
    print "directory now changed\n"
    os.chdir(r"C:\Users\I326017\Downloads\prank\prank")
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))

    print file_list

rename_files()
