"""
Developer: HQSoftware
_______________________________________________________________________________________________________
Description: This is a file deletion program that asks you for an extension(.mp3, .pdf, .docx, etc)
of a file to delete all of the files in a dir that have that extension.
_______________________________________________________________________________________________________
"""

import os
import time

#get users current dir
cwd = os.getcwd()
print("**************************************************************************")
print("Current dir: {0}".format(cwd))
print("**************************************************************************")
print("")

#change user dir
print("Please follow appropriate path format for your OS")
print("********************************************************************************")
print("MacOS path ex: /Users/mycomputer/Desktop")
print("Windows path ex: C:\\Users\\mycomputer\\Desktop")
print("")
new_dir = input("Please enter dir where most files you want to delete are: ")
os.chdir(new_dir)
print("")
cwd = os.getcwd()
print("New dir:", cwd)
print("********************************************************************************")
print("")

ext = input("What extensions would you like to delete: ")

print("")
print("Files:")
print("********************************************************************************")

#show and remove files
for files in os.listdir(cwd):
    if files.endswith(ext):
        print("Removing file........")
        print(files)
        time.sleep(3)
        os.remove(files)