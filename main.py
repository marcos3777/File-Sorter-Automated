import os, shutil 
import time 
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while observer.isAlive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()

path = r"C:/Users/Thanatos/Downloads/"

os.listdir(path)

file_name = os.listdir(path)

folder_names = ['img files', 'doc files', 'torrent files', 'exe files', 'video files', 'code files']

for loop in folder_names:
    if not os.path.exists(path + loop):
        os.mkdir(path + loop)

for file in file_name:
    if file.endswith('.jpg') or file.endswith('.png') or file.endswith('jpeg') and not os.path.exists(path + 'img files/' + file):
        shutil.move(path + file, path + 'img files')
    elif file.endswith('.doc') or file.endswith('.docx') or file.endswith('.pdf')  and not os.path.exists(path + 'doc files/' + file):
        shutil.move(path + file, path + 'doc files')
    elif file.endswith('.torrent'):
        shutil.move(path + file, path + 'torrent files') and not os.path.exists(path + 'torrent files/' + file)
    elif file.endswith('.exe') and not os.path.exists(path + 'exe files/' + file):
        shutil.move(path + file, path + 'exe files')
    elif file.endswith('.mp4') or file.endswith('.mkv') and not os.path.exists(path + 'video files/' + file):
        shutil.move(path + file, path + 'video files')
    elif file.endswith('.py') or file.endswith('.js') or file.endswith('.html') and not os.path.exists(path + 'code files/' + file):
        shutil.move(path + file, path + 'code files')
    else:
        pass

    #Até esse ponto o codigo esta funcionando normalmente. A partir daqui tentarei automatizar usando watchdog

