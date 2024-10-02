import os, shutil 
path = r"C:/Users/Thanatos/Downloads/"

os.listdir(path)

file_name = os.listdir(path)

folder_names = ['img files', 'doc files', 'torrent files', 'exe files']

for loop in folder_names:
    if not os.path.exists(path + loop):
        os.mkdir(path + loop)

for file in file_name:
    if file.endswith('.jpg') or file.endswith('.png') and not os.path.exists(path + 'img files/' + file):
        shutil.move(path + file, path + 'img files')
    elif file.endswith('.doc') or file.endswith('.docx'):
        shutil.move(path + file, path + 'doc files')
    elif file.endswith('.torrent'):
        shutil.move(path + file, path + 'torrent files')
    elif file.endswith('.exe'):
        shutil.move(path + file, path + 'exe files')
    else:
        pass