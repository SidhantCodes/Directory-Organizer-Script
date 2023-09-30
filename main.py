import os
import shutil

targetFolder = 'C:/Users/Sidhant Mishra/Downloads'

ext = {item.split('.')[-1] for item in os.listdir(targetFolder) if os.path.isfile(os.path.join(targetFolder, item))}

for extension in ext:
    if not os.path.exists(os.path.join(targetFolder, extension)):
        os.mkdir(os.path.join(targetFolder, extension))