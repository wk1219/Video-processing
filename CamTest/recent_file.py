import os
import glob

folder = "C:/Users/sjms1\\Desktop\\video\\*"
file_path = glob.glob(folder)

print(file_path)
files = sorted(glob.iglob(file_path), key=os.path.getctime, reverse=True)

