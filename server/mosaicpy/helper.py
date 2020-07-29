import os

def createFolders(img_folders):

    "creates all the necessary folders for the programm to run if not already there"
    for i in range(len(img_folders)):
        path = img_folders[i]        
        os.makedirs(path, exist_ok=True)
