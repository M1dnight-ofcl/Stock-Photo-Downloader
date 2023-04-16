import customtkinter as tk, spid.spid as m, time

class bl_main:
  def set():
    if level == 0:
      return []
    if level == 1:
      return ["I", "I've", "I'd", "I'm", "Me", 
            "You", "Your", "You're", "He", "Him",
           "His", "He'd", "He'll", "Her", "Hers",
           "She", "She'd", "She'll", "They", "Them",
           "They'd", "They'll", "You'll", "I'll", "We",
           "We'll", "We'd", "Us", "My", "Mine"]
    if level == 2:
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
    if level == 3:
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
    print("[INFO] blacklisting level selected", )
  
  def script():
    global key, kg
    key = tk.IntVar()

    def setkey(self):
      global level
      if kg.get() == "No Filtering":
        level = 0
      if kg.get() == "Minor Filtering":
        level = 1
      if kg.get() == "Medium Filtering":
        level = 2
      if kg.get() == "Maximum Filtering":
        level = 3
      key.set(kg.get())
    kg = tk.CTkComboBox(m.frame,
                        values=["No Filtering", "Minor Filtering", "Medium Filtering", "Maximum Filtering"],
                        command=setkey)
    kg.set("No Filtering")
    kg.pack()
    kg.wait_variable(key)
    kg.pack_forget()