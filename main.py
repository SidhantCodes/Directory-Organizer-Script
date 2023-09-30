import os
import shutil

targetFolder = 'insert url'

ext = {item.split('.')[-1] for item in os.listdir(targetFolder) if os.path.isfile(os.path.join(targetFolder, item))}

for extension in ext:
    if not os.path.exists(os.path.join(targetFolder, extension)):
        os.mkdir(os.path.join(targetFolder, extension))
        
        
for item in os.listdir(targetFolder):
    if os.path.isfile(os.path.join(targetFolder, item)):
        fileExt = item.split('.')[-1]
        
        shutil.move(os.path.join(targetFolder, item), os.path.join(targetFolder, fileExt, item))
        