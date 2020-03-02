from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time


class MyHandler(FileSystemEventHandler):
    i = 1

    def on_modified(self, event):
        new_name = "new_file_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(os.path.join(folder_destination, new_name))
            while file_exists:
                self.i += 1
                new_name = "new_file_" + str(self.i) + ".txt"
                file_exists = os.path.isfile(os.path.join(folder_destination, new_name))
            src = os.path.join(folder_to_track, filename)
            new_destination = os.path.join(folder_destination, new_name)
            os.rename(src, new_destination)


# Home Computer:
# folder_to_track = r'C:\Users\Antho\OneDrive\Desktop\trackedFolder'
# folder_destination = r'C:\Users\Antho\OneDrive\Desktop\destinationfolder'

# Laptop:
folder_to_track = r'C:\Users\Anthony Perugini\Desktop\Tracked_Folder'
folder_destination = r'C:\Users\Anthony Perugini\Desktop\Destination_Folder'


event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
