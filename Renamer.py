import os
import re

# Initialize the current working directory, this script should be run in the 
# same folder as the target folders

path = os.path.dirname(__file__)

# Define the pattern for the regex filter
namePattern = re.compile(r"""^(.*?) # Name (group 1)
    [-.] # splitter
    ([0-9]{4}) # Year (group 2)
    [-.] # splitter
    (.*?) # Resolution (group 3)
    [-.] # splitter
    (.*?) # Ripped format (Bluray, Webrip...) (group 4)
    [-.] # splitter
    ([xXhH][0-9]{3}) # Codec (group 5)
    [-.] # splitter
    (.*)$ # Ripping group (Rarbg, yify...) (group 6)
""", re.VERBOSE)

# Define function that walks only 1 level of the directory, to avoid entering subdirectories
def walkLevel(directory, level=1):
    directory = directory.rstrip(os.path.sep)
    assert os.path.isdir(directory)
    numSep = directory.count(os.path.sep)
    for walkRoot, walkDirs, walkFiles in os.walk(directory):
        yield walkRoot, walkDirs, walkFiles
        numSepThis = root.count(os.path.sep)
        if numSep + level <= numSepThis:
            del dirs[:]

if __name__ == "__main__":

# Iterate over all the files and directories
    for root, dirs, files in walkLevel(path):
        for dir_name in dirs:
            match = re.search(namePattern, dir_name)
            if match:
                # Extract the captured substrings
                title = match.group(1).replace('.', ' ')
                year = match.group(2)
                resolution = match.group(3)
                codec = match.group(5)

                # Construct the new name
                new_dir_name = f"{title} ({year})({resolution},{codec})"

                # Print the change 
                print(f"\nChanged file from -> \n[ {dir_name} ]\nto \n[ {new_dir_name} ]\n")
                
                # Rename the directory
                os.rename(dir_name, new_dir_name)

        for file_name in files:
            
            if file_name.endswith('.mp4') or file_name.endswith('.mkv') or file_name.endswith('.srt'):
                
                # Get the file extension 
                file_extension = file_name[-4:]
                # Get the folder name
                folder_name = re.split('/', root)[-1]

                # Check if the file name is already the same as the new directory name
                if file_name[:-4] != folder_name:
                    # Construct the new file name
                    new_file_name = f"{folder_name}{file_extension}"
                    # Print the change
                    print(f"\nChanged file from -> \n[ {file_name} ]\nto \n[ {new_file_name} ]\n")
                    # Rename the file
                    os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))
