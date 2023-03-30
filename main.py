import pvleopard as pv, tqdm as t, os, shutil as s, core.scripts.blacklist as blacklist, core.scripts.fileScan as fs, core.scripts.spellCheck as sc, random as r
from simple_image_download import simple_image_download as simp
from datetime import datetime

vnum = "1.8.5"

x = open("core/assets/logo.txt", "r")
print(x.read())
x.close()

print("\ncurrent version: " + vnum + "\nM1dnightDev (c) 2023\n")

for i in t.tqdm(range(0, 1), desc="creating 'simple_image_download' object"):
  response = simp.simple_image_download

try:
  for i in t.tqdm(range(0, 1), desc="importing 'moviepy.editor' module"):
    import moviepy.editor as mpe
except:
  print("[ERROR] moviepy.editor import failed")

for i in t.tqdm(range(0, 1), desc="retrieving pvleopard access key"):
  lp = pv.create("+K4flsmR4HwbiKOUGOeN4KyvNs5wV20EgOEiBaHbcYUImIwrVrubKQ==")

ogVid = input("What video what you like to download stock images for?\n")

log = open("core/log.txt", "a+")
log.write("\n-----------------------------------------\n" + str(datetime.now()) + " [NEW_FILE] | file uploaded '" + os.path.basename(ogVid) + "'\n")

try:
  os.mkdir("temp")
except:
  print("[INFO] temp folder exists, this may be due to incorrect shutdown")
  s.rmtree("temp")
  os.mkdir("temp")

fpath = "output/" + os.path.basename(ogVid).replace(".mp4", "") + "/"

try:
  video = mpe.VideoFileClip(ogVid)
  try:
    os.mkdir(fpath)
  except:
    print("[INFO] script has been run on video before, clearing old dir")
    s.rmtree(fpath)
    os.mkdir(fpath)
  video.audio.write_audiofile("temp/exportAudio.mp3")
  blacklist.script()
  for i in t.tqdm(range(0, 1), desc="getting video captions"):
    transcript, words = lp.process_file("temp/exportAudio.mp3")
  for i in t.tqdm(range(0, 1), desc="writing video captions to 'exportedCaption.txt'"):
    with open("temp/exportedCaption.txt", "w") as f:
      for word in words:
        final = "%s " % (word.word)
        f.write(final)
  final = sc.check(final)
  print("[WARNING] speech to text may be inaccurate. it may run into errors.\nif you are unhappy with an image downloaded, you may download your own.")
  print("FINAL TRANSCRIPTION:\n" +
        open("temp/exportedCaption.txt", "r").read())
  log.write("video transcription:\n" + open("temp/exportedCaption.txt", "r").read() + "\n")
  cap = open("temp/exportedCaption.txt", "r").read()
  print("[INFO] imported 'exportedCaption.txt'")
  all = cap.split(" ")
  for i in all:
    if i == "":
      del all[all.index(i)]
  print("[INFO] split text to array")
  ie = 1
  for rep in all:
    query = rep + " stock photo"
    if rep.capitalize() in blacklist.list:
      print("[INFO] '" + query + "' was found in blacklist")
    else:
      try:
        for i in t.tqdm(range(0, 1), desc="[INFO] downloading '" + query + "' " + str(ie) +"/" + str(len(all))):
          response().download(query, 10)
        fs.checkFiles("simple_images/" + query, False)
        for i in range(1, 5):
          os.remove("simple_images/" + query + "/" + query + "_" + str(i) + ".jpg")
          # print("removed", "simple_images/" + query + "/" + query + "_" + str(i) + ".jpg")
        working = os.listdir("simple_images/" + query)
        if working:
          finalFile = str(r.choice(working))
          s.move("simple_images/" + query + "/" + finalFile, fpath + finalFile)
          os.rename(fpath + finalFile, fpath + str(ie) + "-" + rep + ".jpg")
          log.write("\ncreated " + fpath + str(ie) + "-" + rep + ".jpg for " + os.path.basename(ogVid))
          ie = ie + 1
        elif not working:
          print("[INFO] download failed, this may be due to photoless term")
      except Exception as e:
        print("[INFO] " + str(e) + " " + str(ie) + "/" + str(len(all)))
        fs.checkFiles(fpath, False)
        ie = ie + 1
  for i in t.tqdm(range(0, 1), desc="[INFO] clearing temp files"):
    s.rmtree("simple_images")
    s.rmtree("temp")
  fs.checkFiles(fpath, False)
  print("\nscript finished, check output for results")
  log.write("\n\nscript finished with no issue\n")
  log.close()
except Exception as e:
  print("[ERROR] ", str(e))
  log.write("\n\nscript finished due to error:\n" + str(e))
  log.close()
