import os
import shutil
import time




def sortDir(targetFolder):
    ext = {item.split('.')[-1] for item in os.listdir(targetFolder) if os.path.isfile(os.path.join(targetFolder, item))}

    for extension in ext:
        if not os.path.exists(os.path.join(targetFolder, extension)):
            os.mkdir(os.path.join(targetFolder, extension))
            
            
    for item in os.listdir(targetFolder):
        if os.path.isfile(os.path.join(targetFolder, item)):
            fileExt = item.split('.')[-1]
            
            shutil.move(os.path.join(targetFolder, item), os.path.join(targetFolder, fileExt, item))
            
if __name__ == '__main__':
    targetFolder = 'Direcrtory URL'
    breakTime_mins = 10
    
    while True:
        sortDir(targetFolder)
        time.sleep(breakTime_mins * 60);