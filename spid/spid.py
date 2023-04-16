# import modules
import pvleopard as pv, tqdm as t, os, shutil as s, random as r, customtkinter as tk, sys, tkinter as tk2
# import local
import spid.scripts.fileScan as fs, spid.scripts.spellCheck as sc, spid.spid as m
# import classes/functions from  modules
from simple_image_download import simple_image_download as simp
from datetime import datetime
import spid.scripts.blacklist as bls
from tkinter.filedialog import askopenfile
from PIL import ImageOps, Image

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

vnum = "2.2"
root = tk.CTk()
frame = tk.CTkFrame(master=root)
blacklist = bls.bl_main

class spid_functions:
  stxt = tk.CTkLabel(root, text = "Script has begun initializing, this may take a minute.")
  def loadUi():
    root.protocol("WM_DELETE_WINDOW", spid_functions.on_closing)
    logo.pack()
    btn1.pack_forget()
    spid_functions.stxt.pack()

  def rm_element():
    spid_functions.stxt.pack_forget()

  def disablecf():
    root.destroy()
    
  def on_closing():
    if tk2.messagebox.askokcancel("Quit Confirmation", "Do you want to quit?"):
      root.destroy()

  def main():
    while True:
      get = askopenfile(mode='r', filetypes=[('Video Files', '*.mp4 *.mpeg *.mov'), ('All Files', "*.")])
      try:
        with get as file:
          global ogVid
          ogVid = os.path.relpath(file.name)
          break
      except:
        print("[INFO] file upload denied")
    spid_main.scriptRunner()

class spid_main:
  def script():
    for i in t.tqdm(range(0, 1), desc="creating 'simple_image_download' object"):
      response = simp.simple_image_download
  
    try:
      for i in t.tqdm(range(0, 1), desc="importing 'moviepy.editor' module"):
        import moviepy.editor as mpe
    except:
      print("[ERROR] moviepy.editor import failed")

    for i in t.tqdm(range(0, 1), desc="retrieving pvleopard access key"):
      lp = pv.create("+K4flsmR4HwbiKOUGOeN4KyvNs5wV20EgOEiBaHbcYUImIwrVrubKQ==")
  
    log = open("spid/log.txt", "a+")
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
      spid_functions.rm_element()
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
      print("FINAL TRANSCRIPTION:\n" + open("temp/exportedCaption.txt", "r").read())
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
        if rep.capitalize() in blacklist.set():
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
      tk.CTkLabel(root, text = "Script has finished! Check the output folder").pack()
      root.protocol("WM_DELETE_WINDOW", spid_functions.disablecf)
    except Exception as e:
      exception_type, exception_object, exception_traceback = sys.exc_info()
      ln = exception_traceback.tb_lineno
      print("[ERROR] ", str(e), "\nline:", ln)
      log.write("\n\nscript finished due to error:\n" + str(e))
      log.close()
      root.protocol("WM_DELETE_WINDOW", spid_functions.disablecf)

  def scriptRunner():
    spid_functions.loadUi()
    spid_main.script()

print(open("spid/assets/logo.txt", "r").read())
print("\ncurrent version: " + vnum + "\nM1dnightDev (c) 2023\n")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

downscale_factor_width = 1.5
downscale_factor_height = 2

window_width = int(round(screen_width/downscale_factor_width))
window_height = int(round(screen_height/downscale_factor_height))

window_dimensions = str(window_width) + "x" + str(window_height)

root.title('SPID - Stock Photo Image Downloader')
root.geometry(window_dimensions) 

photo = Image.open("spid/assets/logo.png")
logo_image_source_aspect_ratio = photo.width/photo.height
logo_width = photo.width/logo_image_source_aspect_ratio
logo_height = photo.height/logo_image_source_aspect_ratio
logoImg = tk.CTkImage(photo, size=(logo_width, logo_height))
logo = tk.CTkLabel(frame, text = '', image = logoImg)

btn1 = tk.CTkButton(frame,
	text = 'Upload Video',
	command = spid_functions.main)

frame.pack(pady=20, padx=20, fill="both", expand=True)
logo.pack()
btn1.pack()

root.mainloop()
