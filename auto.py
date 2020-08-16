from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

import os
import json
import time

class Myhandler(fileSystemEventHandler):
    i = 1
    def on_modified(self, event):
    new_name = "new_file"+ str(self.i) + ".txt"
    for filename in os.listdir(folder_to_track):
        file.exists= os.path.isfile(folder_destination + "/" + new_name)
        while file_exsist:
            self.i += 1
            new_name = "new_file"+ str(self.i) + ".txt"
            file_exsist = os.pathisfile(folder_destination + "/" + new_name)


        src = folder_to_track + "/"+ filename
        new_destination = folder_destination + "/" + new_name
        os.rename(src, new_destination)



    






    folder_to_track = "\Users\Åmar\Desktop\myFolder"
    folder_destination = "\Users\Åmar\Desktop\myFolder"
    EventHandler = Myhandler()
    Observer=Observer()
    Observer.Schedule(Event_Handler, folder_to_track, recursive = True)
    Observer.start
    


    try:
        while True: 
                time.sleep(10)

     except KeyboardInterrupt.     