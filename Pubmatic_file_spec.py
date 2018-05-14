import hashlib
import time
import os
import shutil

#Get SHA1 hash of file contents
def file_hash(filepath):
    h = hashlib.sha256()
    with open(filepath, 'rb', buffering=0) as f:
        for b in iter(lambda: f.read(128*1024), b''):
            h.update(b)
    return h.hexdigest()


#Specify path for downloaded file, so we can rename it according to the file spec
path = "C:/Users/Elena/Downloads"


#Get last downloaded file
filename = max([path + "/" +  f for f in os.listdir(path)], key=os.path.getctime)

datestamp = time.strftime("%Y-%m-%d")
publisher = 'Pubmatic'
hash = file_hash(filename)
print(hash)
status = ''
ext = '.csv'
new_name = datestamp + '_' + publisher + '_' + hash + status + ext

