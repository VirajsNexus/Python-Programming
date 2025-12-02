import os

# specify the path of directory to list files
directory = '/Users/Viraj/OneDrive/Desktop/Python Full Course'

#list all files present in the specified directory
files= os.listdir(directory)

# print(files) //simple way to print files without loop

#print each file preset in the directory
for items in files:
    print(items)