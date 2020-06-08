#***********************************************
# Developer: Jeyamaruthi Jayakumar             *
# UTA ID: 1001757737                           *
# Objective: To automate the organization      *
# of files into its specific extension         *
# Date: 07/06/2020                             *
#***********************************************

import os
import glob as g

List_of_file = g.glob("*") #Get all files from the specific folder
#print(List_of_file)

extension_set = set() #for unique extensions
for file in List_of_file:
    extension = file.split(sep = ".") #automatically fetches extensions from the existing file.
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue

#print(extension_set)

def createDirs():
    for directory in extension_set:
        try:
            os.makedirs(directory+"_files") #Naming conversions for Directory
                                            #(e.g. Folder/Directory => pdf_files)
        except FileExistsError:
            continue


def arrange():
    for file in List_of_file:
        fextension = file.split(sep = '.') #fetch the avaiable extension of a file
        try:
            os.rename(file,fextension[1]+"_files/"+file) #Re-Naming the Directory
                                                         #(e.g. Folder/Directory => pdf_files)
        except (OSError, IndexError):
            continue

createDirs()  #Call the method to create the directory
arrange()     #Call the method to arrange

## Developed by Jeyamaruthi Jayakumar
