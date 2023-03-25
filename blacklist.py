import getkey as k

def script():
  global list, level
  print("What level of blacklisting would you like")
  print("[0]: skip filtering")
  print("[1]: simple pronouns (removes terms like: I, Me, You)")
  print("[2]: basic terms (filters for unnecessary words in sentence)")
  print("[3]: unimportant terms (only allows from prominant words)")
  key = k.getkey()
  if key == "0":
    level = int(key)
    list = []
  if key == "1":
    level = int(key)
    list = ["I", "I've", "I'd", "I'm", "Me", 
            "You", "Your", "You're", "He", "Him",
           "His", "He'd", "He'll", "Her", "Hers",
           "She", "She'd", "She'll", "They", "Them",
           "They'd", "They'll", "You'll", "I'll", "We",
           "We'll", "We'd", "Us", "My", "Mine"]
  if key == "2":
    level = int(key)
    list = ["I", "I've", "I'd", "I'm", "Me", 
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
  if key == "3":
    level = int(key)
    list = ["I", "I've", "I'd", "I'm", "Me", 
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