from gingerit.gingerit import GingerIt

def check(msg):
  global parser
  parser = GingerIt()
  parser.parse(msg)