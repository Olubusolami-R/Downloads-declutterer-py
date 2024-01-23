import os
from pathlib import Path

#Step 1: Highlight the folder names in a dictionary
folder_names = {
    "Audio": {'aif','cda','mid','midi','mp3','mpa','ogg','wav','wma'},
    "Compressed":{'7z','deb','pkg','rar','rpm', 'tar.gz','z', 'zip'},
    'Code':{'js','jsp','html','ipynb','py','c','css', 'ts','tsx'},
    'Epubs':{'epub'},
    'PDFs':{'pdf'},
    'Images':{'bmp','gif','ico','jpeg','jpg','png','jfif','svg','tif','tiff','heic','webp'},
    'Other Documents':{'ppt','pptx','xls', 'xlsx','doc','docx','txt', 'tex'},
    'Software':{'apk','bat','bin', 'exe','jar','msi','dmg'},
    'Videos':{'3gp','avi','flv','h264','mkv','mov','mp4','mpg','mpeg','wmv'},
    'Others': {'NONE'}
}

#Step 2: Create a dictionary that maps an extension to its corresponding folder from the above dictionary
#Step 3: State download folder path
#Step 4: Access the download folder and store the filepaths in a list
#Step 5: Access the download folder and store the filepaths in a list
#Step 6: Create folder paths
#Step 7: Create folders from paths
#Step 8: Create function that creates new paths for files 
#Step 9: Use the function to rename al; the files from 4
#Step 10: Move existing folders to into the newly created "Others" folder.


