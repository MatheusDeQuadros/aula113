import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHand

from_dir= "C:\Users\mathe\Desktop\Download_Fake"
to_dir= "C:\Users\mathe\Desktop\Pasta_organizadora"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileMovementHandler) :
    
    def on_created(self, event):
        print(event)
        print(event.src_path)


# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileMovementHandler()

# Inicialize o Observer
observer = Observer()

# Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Inicie o Observer
observer.start()


while True:
    time.sleep(2)
    print("executando...")
