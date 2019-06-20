import os

mypath = "images"

for (dirpath, dirnames, filenames) in os.walk(mypath):
    fid = 1
    for f in filenames:
        os.rename(os.path.join(dirpath, f), os.path.join(dirpath, "{:06d}.jpg".format(fid)))
        fid += 1
    break