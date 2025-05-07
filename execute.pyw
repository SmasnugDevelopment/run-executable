import os, shutil
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

try:
    os.mkdir(os.environ["USERPROFILE"] + "\\AppData\\Roaming\\Python")
except:
    pass
try:
    os.mkdir(os.environ["USERPROFILE"] + "\\AppData\\Roaming\\Python\\Python312")
except:
    pass
try:
    os.mkdir(os.environ["USERPROFILE"] + "\\AppData\\Roaming\\Python\\Python312\\Scripts")
except:
    pass

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
file = askopenfilename() # show an "Open" dialog box and return the path to the selected file
filename = str(file).split("/")[-1]

try:
    shutil.rmtree(os.environ["USERPROFILE"] + "\\AppData\\Roaming\\Python\\Python312\\Scripts\\e")
except:
    pass

os.mkdir(os.environ["USERPROFILE"] + "\\AppData\\Roaming\\Python\\Python312\\Scripts\\e")


shutil.copy(file, os.environ["USERPROFILE"] + "\\AppData\\Roaming\\Python\\Python312\\Scripts\\e\\")

os.system(os.environ["USERPROFILE"] + "\\AppData\\Roaming\\Python\\Python312\\Scripts\\e\\" + filename)