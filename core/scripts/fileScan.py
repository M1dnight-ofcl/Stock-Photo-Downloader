from os import listdir, remove
from PIL import Image

def checkFiles(dir):
  for filename in listdir(dir):
    try:
      img = Image.open(dir+ "/" +filename)
      img.verify()
    except (IOError, SyntaxError) as e:
      print('Corrupted file:', filename, "\n" + str(e))
      remove(dir + "/" + filename)