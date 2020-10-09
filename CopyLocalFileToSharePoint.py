#  How to copy a local file to an O365 SharePoint / Teams folder?
#
# * Open the SharePoint site in your browser, or your Teams in the Teams application
# * Navigate to the receiving folder
# * Clic the "Sync" button, and allow/agree with popup for OneDrive
# * Wait a few second and check with your file explorer that the corresponding folder has been added  
#   'C:\Users\YourUser\YourCompany\YourSharePointSite - YourDestinationFolder'

import os     # to read env variable
import shutil # for the copy itself

# Source file you want to upload to O365
LocalFile = './YourFile.txt' # relative path from work dir, you can of course use an absolute path

# Destination
userprofile = os.environ['USERPROFILE'] # return C:\Users\YourUser
DestinationDirectory = userprofile + r'\YourCompany\YourSharePointSite - YourDestinationFolder' 

# Copy
shutil.copy(LocalFile, DestinationDirectory)
# Allow a few seconds for your OneDrive to synchronize files with SharePoint
