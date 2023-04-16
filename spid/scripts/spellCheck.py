from gingerit.gingerit import GingerIt
import openai

openai.api_key = "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"

def check(msg):
  global parser
  gi = GingerIt()
  gi.parse(msg)
#  FOR LATER =====================================
#  response = openai.ChatCompletion.create(
#    model="gpt-3.5-turbo",
#    messages=[
#            {"role": "system", "content": "You are a chatbot"},
#            {"role": "user", "content": "Why should DevOps engineer learn kubernetes?"},
#        ]
#  )
#  result = ''
#  for choice in response.choices:
#    result += choice.message.content