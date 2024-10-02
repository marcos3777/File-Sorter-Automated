import os
import shutil
import logging
from posixpath import splitext
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source_dir = "C:/Users/Thanatos/Downloads"
dest_dir_torrent = "C:/Users/Thanatos/Downloads/torrent files"
dest_dir_video = "C:/Users/Thanatos/Downloads/video files"
dest_dir_image = "C:/Users/Thanatos/Downloads/img files"
dest_dir_documents = "C:/Users/Thanatos/Downloads/doc files"
dest_dir_code = "C:/Users/Thanatos/Downloads/code files"
dest_exe = "C:/Users/Thanatos/Downloads/exe files"

image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico"]
video_extensions = [".webm", ".mp4", ".avi", ".mov", ".mkv"]
torrent_extensions = [".torrent"]
document_extensions = [".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
code_extensions = [".py", ".html", ".css", ".js", ".cpp", ".c", ".java", ".php", ".sql", ".json", ".xml", ".md", ".txt"]
installer_extensions = [".exe", ".msi"]


dest_dirs = [dest_dir_torrent, dest_dir_video, dest_dir_image, dest_dir_documents, dest_dir_code]
for folder in dest_dirs:
    if not os.path.exists(folder):
        os.makedirs(folder)

def makeUnique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while os.path.exists(os.path.join(dest, name)):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

def move_files(dest, entry, name):
    dest_path = os.path.join(dest, name)
    if os.path.exists(dest_path):
        unique_name = makeUnique(dest, name)
        dest_path = os.path.join(dest, unique_name)
    shutil.move(entry.path, dest_path)
    logging.info(f"Moved {entry.path} to {dest_path}")

class MoveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with os.scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                if entry.is_file(): 
                    self.check_torrent_files(entry, name)
                    self.check_video_files(entry, name)
                    self.check_image_files(entry, name)
                    self.check_document_files(entry, name)
                    self.check_code_files(entry, name)
                    self.check_installer_files(entry, name)

    def check_torrent_files(self, entry, name):
        if any(name.endswith(ext) for ext in torrent_extensions):
            move_files(dest_dir_torrent, entry, name)

    def check_video_files(self, entry, name):
        if any(name.endswith(ext) for ext in video_extensions):
            move_files(dest_dir_video, entry, name)

    def check_image_files(self, entry, name):
        if any(name.endswith(ext) for ext in image_extensions):
            move_files(dest_dir_image, entry, name)

    def check_document_files(self, entry, name):
        if any(name.endswith(ext) for ext in document_extensions):
            move_files(dest_dir_documents, entry, name)

    def check_code_files(self, entry, name):
        if any(name.endswith(ext) for ext in code_extensions):
            move_files(dest_dir_code, entry, name)

    def check_installer_files(self, entry, name):
        if any(name.endswith(ext) for ext in installer_extensions):
            move_files(dest_exe, entry, name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    patch = source_dir
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, patch, recursive=True)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    finally:
        observer.stop()
        observer.join()
