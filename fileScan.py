from os import listdir, remove
from PIL import Image

def checkFiles(dir):
  for filename in listdir(dir):
    if filename.endswith('.jpg'):
      try:
        img = Image.open(dir+ "/" +filename)
        img.verify()
      except (IOError, SyntaxError) as e:
        print('Bad file: ', filename)
        remove(dir + "/" + filename)