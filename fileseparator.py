import os, shutil
from tkinter import *


dict_extensions = {
    'audio' : ('.mp3', '.m4a', '.wav', '.flac'),
    'video' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'document' : ('.doc', '.pdf', '.txt','.ppt','.pptx'),
    'image' : ('JPEG ', 'JPG',' PNG ','GIF','.png','.jpg','jpeg' )
}


folderpath = input('enter folder path : ')

def file_finder(folder_path, file_extensions):
     files = []
     for file in os.listdir(folder_path):
         for extension in file_extensions:
             if file.endswith(extension):
                 files.append(file)
     return files
    #above code in one line
    #return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]


for extension_type, extension_tuple in dict_extensions.items():
     lst=file_finder(folderpath, extension_tuple)
     l=len(lst)
     print(extension_type,"--",l)
     #if any file type does not exists then donot nake the folder of it
     if l>=1:
         #making folder name
         folder_name = extension_type + ' Files'
         #making folder path
         folder_path = os.path.join(folderpath, folder_name)
         #checking if the fplder already exits or not
         if os.path.exists(folder_path):
             pass
         else:
             os.makedirs(folder_path)
         for item in lst:
             item_path = os.path.join(folderpath,item)
             item_new_path = os.path.join(folder_path,item)
             shutil.move(item_path,item_new_path)
   

