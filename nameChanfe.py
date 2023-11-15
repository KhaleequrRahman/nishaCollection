import os

folder_path = 'C:\\Users\\khaleeq\\Documents\\sageerWebsite\\Broom'

# List all files in the folder
files = os.listdir(folder_path)

# Iterate through each file and rename it
for i, file_name in enumerate(files):
    # Define the new name using a pattern or any logic you want
    new_name = f"image_{i+1}.jpg"
    
    # Construct the full paths
    old_path = os.path.join(folder_path, file_name)
    new_path = os.path.join(folder_path, new_name)
    
    # Rename the file
    os.rename(old_path, new_path)

print("Renaming complete!")