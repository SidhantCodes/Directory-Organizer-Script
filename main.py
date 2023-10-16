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

            if item.lower() == 'desktop.ini':
                continue
            
            src = os.path.join(targetFolder, item)
            dst = os.path.join(targetFolder, fileExt, item)
            
            try:
                shutil.move(src, dst)
            except PermissionError as e:
                print(f"Error moving {src} to {dst}: {e}")
                continue

if __name__ == '__main__':
    targetFolder = 'URL/TO/TARGET/FOLDER'
    breakTime_mins = 10
    
    while True:
        sortDir(targetFolder)
        time.sleep(breakTime_mins * 60)
