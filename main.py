import pvleopard as pv, tqdm as t, os, downloader as d, shutil as s
from simple_image_download import simple_image_download as simp

vnum = "1.0"

x = open("assets/logo.txt", "r")
print(x.read())
x.close()
print("\n current version: " + vnum + "\n")

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
ogVid = input("What video what you like to download stock images for?\n")

try:
  video = mpe.VideoFileClip(ogVid)
  try:
    print("[INFO] 'exportAudio.mp3' file exists; deleting file...")
    os.remove("exportAudio.mp3")
  except:
    print("[INFO] 'exportAudio' non-existant; skipping deletion...")
  video.audio.write_audiofile("exportAudio.mp3")
  for i in t.tqdm(range(0, 1), desc ="getting video captions"):
    transcript, words = lp.process_file("exportAudio.mp3")
  for i in t.tqdm(range(0, 1), desc ="writing video captions to 'exportedCaption.txt'"):
    with open("exportedCaption.txt", "w") as f:
      for word in words:
        final = "%s " % (word.word)
        f.write(final)
  print("[WARNING] speech to text may be inaccurate. it may run into errors.\nif you are unhappy with an image downloaded, you may download your own.")
  print("FINAL TRANSCRIPTION:\n" + open("exportedCaption.txt", "r").read())
  cap = open("exportedCaption.txt", "r").read()
  print("[INFO] imported 'exportedCaption.txt'")
  all = cap.split(" ")
  print("[INFO] split text to array")
  ie = 0
  try:
    print("[INFO] wiping downloads folder...")
    try:
      s.rmtree("simple_images")
    except:
      s.rmtree("output")
  except:
    print("[INFO] downloads folder non-existant, skipping deletion...")
  for rep in all:
    query = rep + " stock photo"
    try:
      for i in t.tqdm(range(0, 1), desc = "[INFO] downloading '" + query + "' " + str(ie) + "/" + str(len(all))):
        response().download(query, 5)
      ie = ie + 1
    except:
      print("[INFO] '" + query + "' already downloaded or had error downloading " + str(ie) + "/" + str(len(all)))
      ie = ie + 1
  os.rename("simple_images", "output")
  print("\n[INFO] script finished\nplease note that the module used downloads 4 google images before it downloads the requested stock photo. the requested photo is the fifth one, skip the others. you may also need to refresh to see the changes.")
except:
  print("[ERROR] invalid input")