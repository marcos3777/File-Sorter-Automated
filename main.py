import os, shutil 
path = r"C:/Users/Thanatos/Downloads/"

os.listdir(path)


folder_names = ['img files', 'doc files', 'torrent files', 'exe files']

for loop in folder_names:
    if not os.path.exists(path + loop):
        os.mkdir(path + loop)