import pvleopard as pv, tqdm as t, os, shutil as s, core.scripts.blacklist as blacklist, core.scripts.fileScan as fs, core.scripts.spellCheck as sc, random as r
from simple_image_download import simple_image_download as simp

vnum = "1.7.1"

x = open("core/assets/logo.txt", "r")
print(x.read())
x.close()

print("\ncurrent version: " + vnum + "\n")

for i in t.tqdm(range(0, 1), desc ="creating 'simple_image_download' object"):
  response = simp.simple_image_download

try:
  for i in t.tqdm(range(0, 1), desc ="importing 'moviepy.editor' module"):
    import moviepy.editor as mpe
except:
  print("[ERROR] moviepy.editor import failed")

for i in t.tqdm(range(0, 1), desc ="retrieving pvleopard access key"):
  lp = pv.create("+K4flsmR4HwbiKOUGOeN4KyvNs5wV20EgOEiBaHbcYUImIwrVrubKQ==")
# os.environ['IMAGEIO_FFMPEG_EXE'] = 'ffmpeg'
try:
  print("[INFO] clearing output folder...")
  s.rmtree("output")
  os.mkdir("output")
except:
  print("[INFO] output clear failed, trying to create new...")
  try:
    print("[INFO] output folder created")
    os.mkdir("output")
  except:
    print("[INFO] output folder wipe failed, skiping step...")
ogVid = input("What video what you like to download stock images for?\n")
amt = 1

try:
  video = mpe.VideoFileClip(ogVid)
  try:
    print("[INFO] 'exportAudio.mp3' file exists; deleting file...")
    os.remove("exportAudio.mp3")
  except:
    print("[INFO] 'exportAudio' non-existant; skipping deletion...")
  video.audio.write_audiofile("exportAudio.mp3")
  blacklist.script()
  for i in t.tqdm(range(0, 1), desc ="getting video captions"):
    transcript, words = lp.process_file("exportAudio.mp3")
  for i in t.tqdm(range(0, 1), desc ="writing video captions to 'exportedCaption.txt'"):
    with open("exportedCaption.txt", "w") as f:
      for word in words:
        final = "%s " % (word.word)
        f.write(final)
  final = sc.check(final)
  print("[WARNING] speech to text may be inaccurate. it may run into errors.\nif you are unhappy with an image downloaded, you may download your own.")
  print("FINAL TRANSCRIPTION:\n" + open("exportedCaption.txt", "r").read())
  cap = open("exportedCaption.txt", "r").read()
  print("[INFO] imported 'exportedCaption.txt'")
  all = cap.split(" ")
  print("[INFO] split text to array")
  ie = 0
  try:
    print("[INFO] wiping downloads folder...")
    s.rmtree("output/")
    os.mkdir("output/")
  except:
    print("[INFO] downloads folder non-existant, skipping deletion...")
  for rep in all:
    query = rep + " stock photo"
    if rep.capitalize() in blacklist.list:
      print("[INFO] '" + query + "' was found in blacklist")
    else:
      try:
        for i in t.tqdm(range(0, 1), desc = "[INFO] downloading '" + query + "' " + str(ie) + "/" + str(len(all))):
          response().download(query, 10)
        fs.checkFiles("simple_images/" + query)
        working = os.listdir("simple_images/" + query)
        for i in range(1,4):
          working.remove(query + "_" + str(i) + ".jpg")
        for i in range(1, amt):
          finalFile = str(r.choice(working))
          s.move("simple_images/" + query + "/" + finalFile, "output/" + finalFile)
          os.rename("output/" + finalFile, "output/" + query + ".jpg")
        ie = ie + 1
      except Exception as e:
        print("[INFO] " + str(e) + " " + str(ie) + "/" + str(len(all)))
        fs.checkFiles("output")
        ie = ie + 1
  s.rmtree("simple_images")
  os.remove("exportAudio.mp3")
  os.remove("exportedCaption.txt")
  fs.checkFiles("output")
  print("\n[INFO] script finished\nplease note that the module used downloads 4 google images before it downloads the requested stock photo. the requested photo is the fifth one, skip the others. you may also need to refresh to see the changes.")
except Exception as e:
  print("[ERROR] ", str(e))