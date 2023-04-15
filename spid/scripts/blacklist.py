import tkinter as tk, spid.spid as m, time

class bl_main:
  def set():
    if kg.get() == 0:
      level = int(kg.get())
      return []
    if kg.get() == 1:
      level = int(kg.get())
      return ["I", "I've", "I'd", "I'm", "Me", 
            "You", "Your", "You're", "He", "Him",
           "His", "He'd", "He'll", "Her", "Hers",
           "She", "She'd", "She'll", "They", "Them",
           "They'd", "They'll", "You'll", "I'll", "We",
           "We'll", "We'd", "Us", "My", "Mine"]
    if kg.get() == 2:
      level = int(kg.get())
      return ["I", "I've", "I'd", "I'm", "Me", 
            "You", "Your", "You're", "He", "Him",
           "His", "He'd", "He'll", "Her", "Hers",
           "She", "She'd", "She'll", "They", "Them",
           "They'd", "They'll", "You'll", "I'll", "We",
           "We'll", "We'd", "Us", "How", "About", "Til",
           "When", "Will", "Why", "If", "Else", "Other",
           "Otherwize", "Likely", "Most", "Another", "Also",
           "My", "Mine", "Only", "To", "From", "While",
           "During", "A", "Photo", "Stock", "The", "This",
           "Those", "Is", "Isn't", "It", "It's", "It'll"]
    if kg.get() == 3:
      level = int(kg.get())
      return ["I", "I've", "I'd", "I'm", "Me", 
            "You", "Your", "You're", "He", "Him",
           "His", "He'd", "He'll", "Her", "Hers",
           "She", "She'd", "She'll", "They", "Them",
           "They'd", "They'll", "You'll", "I'll", "We",
           "We'll", "We'd", "Us", "How", "About", "Til",
           "When", "Will", "Why", "If", "Else", "Other",
           "Otherwize", "Likely", "Most", "Another", "Also",
           "My", "Mine", "Only", "To", "From", "While",
           "During", "A", "Photo", "Stock", "The", "This",
           "Those", "Is", "Isn't", "Nice", "Simple", "Basic",
           "During", "On", "Off", "Cool", "It", "It's", "It'll"]
    print("[INFO] blacklisting level selected", kg.get())
  
  def script():
    global key, kg, btn1
    key = tk.IntVar()
    kg = tk.Scale(m.root,
                 from_=0, to=3,
                 orient='horizontal')
    kg.pack()
    btn1 = tk.Button(m.root,
                     text = 'Submit',
                     command = lambda: key.set(kg.get()))
    btn1.pack()
    btn1.wait_variable(key)
    kg.pack_forget()
    btn1.pack_forget()