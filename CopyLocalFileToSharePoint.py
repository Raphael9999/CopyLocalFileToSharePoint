import os     # to read env variable
import shutil # for the copy itself

def copy_file_to_sp(file, target_dir):
    # Copy
    shutil.copy(file, target_dir)

# Source file you want to upload to O365
LocalFile = './YourFile.txt' # relative path from work dir, you can of course use an absolute path

# Destination
userprofile = os.environ['USERPROFILE'] # return C:\Users\YourUser
# you can overwrite DestinationDirectory with the absolute path of you sync directory 
DestinationDirectory = userprofile + r'\YourCompany\YourSharePointSite - YourDestinationFolder' 

# Call the routine and copy to sync folder
copy_file_to_sp(LocalFile, DestinationDirectory)
# Allow a few seconds for your OneDrive to synchronize the file with O365 SharePoint