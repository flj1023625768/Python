import os
root = '/mnt/kejian/edu-edu/lesson_crs78/self'
file = r'/tmp/nas.txt'
for dirpath,dirnames,filenames in os.walk(root):
    for filename in filenames:
        dirs = os.path.join(dirpath,filename)[11:]
        f = open(file, 'a')
        f.write(str(dirs)+'\n')
