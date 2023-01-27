import os 


# when we will create any file, we need certain directory structure 

# os.path.join("base directory", "child directory") : based on your operating system it will join, wherever joining of path is required you should go for 
dirs = [
    # data directory: raw folder , data: processed folder ( for storing processed file like splitting and all)
    # notebooks file for experimenting in jupyter notebook , for model saving = saved_models file , src folder = for all dataset will go
    # In windows "backslash" is used whereas in linux we use "forwardslash", that's why common platform through "os library"    
    os.path.join("data", "raw"), 
    os.path.join("data", "processed"), 
    "notebooks",
    "saved_models", 
    "src" 

]

# creating above directory structure one by one 

for dir_ in dirs:
    # making directories for this, exist_ok = True,  will restrict further creation of folder every time loop runs
    os.makedirs(dir_, exist_ok=True)
    # All these folders are empty folders & we need to initalize git here too for files version tracking, so will keet empty "gitkeep" file in every empty folder 
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass 


# Now, Let's look at what are the files we need. ".gitignore" files we mention that files which we don't want to push 
# Inside source (src) folder we want to create __init__.py for making source as a python package  
files = [

    "dvc.yaml", 
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")

]

# Now, we need to create those files mentioned above, opening the files and save them by looping over them


for file_ in files:
    with open(file_, "w") as f:
        pass 




