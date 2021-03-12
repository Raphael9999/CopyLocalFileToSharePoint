# CopyLocalFileToSharePoint

## Description
Help you copy a local file to SharePoint online (Office 365)

__Who is this for?__
You are a regular user with access to a SharePoint site within your company environment.  
You do not have access to a service account, security settings, oauth, API, etc.  
You have an O365 account and OneDrive install on your computer.  

__Who is this not for?__
You have access to service account, security settings, oauth, API, etc. Your O365 Admin is willing to help you.  
You will be better of using the office365 api from Microsoft. There are several package that can simplify the process, as an example shareplum.  
You do not have an O365 account, or Microsoft OneDrive is not available  

__How does it work?__
It is a very simple and basic way to copy a local file to a target SharePoint/Teams directory.  
The file will be first copy by the program in your local synchronized copy of the target directory,  
then Microsoft OneDrive will synchronize/upload it to the corresponding O365 SharePoint/Teams folder.  

## Installation
Installation should be straight forward:  
* os and shutil package comes with recent Python, no package installation required  

From the O365 SharePoint, we sync the target folder on your computer:  
* Open the SharePoint site in your browser, or your Teams in the Teams application
* Navigate to the receiving folder
* Clic the "Sync" button, and allow/agree with popup for OneDrive
* Wait a few second and check with your file explorer that the corresponding folder has been added. It should follow the following pattern  
'C:\Users\YourUser\YourCompany\YourSharePointSite - YourDestinationFolder'

## Example
* Follow the Installation process  
* Update DestinationDirectory  
* Run the program, the YourFile.txt should appear after a few seconds in your target O365 SharePoint/Teams folder  

## License
CC0 1.0 Universal  
Raphael Louvrier 2020  
Refer to the LICENSE file  