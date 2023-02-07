import time
import os
import shutil
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/uma/Downloads"
to_dir = "/Users/uma/Desktop/downloadedFiles"

dir_tree ={
    "Image_Files": ['.jpg','.jpeg','.gif','.png','.jfif'],
    "Video_files": ['.mpg','.mp2','.mpeg','.mpv','.mp4','.m4v','.avi','.mov'],
    "Document_Files":['.xls','.ppt','.pdf','.txt','.csv','.xlsx'],
    "Setup_Files":['.exe','.cmd','.dmg','.bin','.msi']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self,event):
        name,extension = os.path.splitext(event.src_path)
        time.sleep(1)

        for key,value in dir_tree.items():
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print("Downloaded " + file_name)

                path1 = from_dir +'/'+file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):
                    print("Directory Exists.. ")
                    if os.path.exists(path3):
                        print("Filename already exists in " + key + "....")
                        print("Renaming file " + file_name + "....")
                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0,99)) + os.path.splitext(file_name)[1]
                        print(new_file_name)
                        path4 = to_dir + '/' + key + '/' + new_file_name
                        print("Moving file " + new_file_name)
                        shutil.move(path1,path4)
                        time.sleep(1)
                    else:
                        print("Moving file " + file_name)
                        shutil.move(path1,path3)
                        time.sleep(1)

                else:
                    print("Making Directory.... ")
                    os.makedirs(path2)
                    print("Moving file " + file_name)
                    shutil.move(path1,path3)
                    time.sleep(1)

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler,from_dir,recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running... ")

except KeyboardInterrupt:
    print("stopped")
    observer.stop()




