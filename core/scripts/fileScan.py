from os import listdir, remove
from PIL import Image

def checkFiles(dir, se):
  for filename in listdir(dir):
    try:
      img = Image.open(dir+ "/" +filename)
      img.verify()
    except (IOError, SyntaxError) as e:
      print('Corrupted file:', filename)
      if se:
        print(e)
      else:
        pass
      remove(dir + "/" + filename)

def verify(dir):
  for filename in listdir(dir):
    try:
      img = Image.open(dir+ "/" +filename)
      img.verify()
      return True
    except (IOError, SyntaxError) as e:
      print('Corrupted file:', filename, "\n" + str(e))
      return False