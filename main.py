import pvleopard as pv, tqdm as t, os, shutil as s, core.scripts.blacklist as blacklist, core.scripts.fileScan as fs, core.scripts.spellCheck as sc, random as r
from simple_image_download import simple_image_download as simp

vnum = "1.8"

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
try:
  os.mkdir("temp")
except:
  print("[INFO] temp folder exists, this may be due to incorrect shutdown")

try:
  video = mpe.VideoFileClip(ogVid)
  video.audio.write_audiofile("temp/exportAudio.mp3")
  blacklist.script()
  for i in t.tqdm(range(0, 1), desc ="getting video captions"):
    transcript, words = lp.process_file("temp/exportAudio.mp3")
  for i in t.tqdm(range(0, 1), desc ="writing video captions to 'exportedCaption.txt'"):
    with open("temp/exportedCaption.txt", "w") as f:
      for word in words:
        final = "%s " % (word.word)
        f.write(final)
  final = sc.check(final)
  print("[WARNING] speech to text may be inaccurate. it may run into errors.\nif you are unhappy with an image downloaded, you may download your own.")
  print("FINAL TRANSCRIPTION:\n" + open("temp/exportedCaption.txt", "r").read())
  cap = open("temp/exportedCaption.txt", "r").read()
  print("[INFO] imported 'exportedCaption.txt'")
  all = cap.split(" ")
  print("[INFO] split text to array")
  ie = 1
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
        fs.checkFiles("simple_images/" + query, False)
        for i in range(1,5):
          os.remove("simple_images/" + query + "/" + query + "_" + str(i) + ".jpg")
          # print("removed", "simple_images/" + query + "/" + query + "_" + str(i) + ".jpg")
        working = os.listdir("simple_images/" + query)
        if working:
          finalFile = str(r.choice(working))
          s.move("simple_images/" + query + "/" + finalFile, "output/" + finalFile)
          os.rename("output/" + finalFile, "output/" + str(ie) + "-" + rep + ".jpg")
          ie = ie + 1
        elif not working:
          print("[INFO] download failed, this may be due to photoless term")
      except Exception as e:
        print("[INFO] " + str(e) + " " + str(ie) + "/" + str(len(all)))
        fs.checkFiles("output", False)
        ie = ie + 1
  for i in t.tqdm(range(0, 1), desc = "[INFO] clearing temp files"):
    s.rmtree("simple_images")
    s.rmtree("temp")
  fs.checkFiles("output", False)
except Exception as e:
  print("[ERROR] ", str(e))